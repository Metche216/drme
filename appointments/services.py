import requests
from datetime import datetime
from decouple import config
from core.models import Appointment, User
import logging

logger = logging.getLogger(__name__)

def get_emr_headers():
    # Fetch a new token every time to avoid expiration issues
    base_url = config('EMR_API_BASE_URL', default='http://localhost:8000/api')
    username = config('EMR_API_USERNAME', default='drme_website')
    password = config('EMR_API_PASSWORD', default='SecureAPI_Password!123')
    
    try:
        resp = requests.post(f"{base_url}/token/", json={
            "username": username,
            "password": password
        })
        resp.raise_for_status()
        token = resp.json()['access']
        return {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
    except Exception as e:
        logger.error(f"Failed to fetch EMR auth token: {e}")
        return {'Content-Type': 'application/json'}

def fetch_appointments(user_email):
    """
    Fetches appointments from the EMR API for the given user.
    Syncs them to the local database to use the existing DrME models.
    """
    base_url = config('EMR_API_BASE_URL', default='http://localhost:8000/api')
    
    # In the EMR, we enabled filtering by patient__email
    url = f"{base_url}/appointments/?patient__email={user_email}"
    
    try:
        response = requests.get(url, headers=get_emr_headers())
        response.raise_for_status()
        events = response.json()
        
        synced_appointments = []
        user = User.objects.filter(email=user_email).first()
        
        for event in events:
            # The EMR returns 'date', 'start_time', 'end_time'
            start_dt_str = f"{event['date']}T{event['start_time']}"
            end_dt_str = f"{event['date']}T{event['end_time']}"
            
            # We repurpose google_event_id to store the EMR Appointment ID
            appt, created = Appointment.objects.update_or_create(
                google_event_id=str(event['id']),
                defaults={
                    "start": datetime.fromisoformat(start_dt_str),
                    "end": datetime.fromisoformat(end_dt_str),
                    "patient": event.get('patient_name', 'Unknown'),
                    "email": user_email,
                    "user": user
                }
            )
            
            # Update status if cancelled in EMR so we don't show it here
            if event.get('status') == 'CANCELLED':
                 appt.delete()
            else:
                 synced_appointments.append(appt)
            
        return synced_appointments
    except Exception as e:
        logger.error(f"Error fetching from EMR: {e}")
        return []

def cancel_appointment_service(appointment_id):
    """
    Cancels an appointment by pinging the EMR API and deleting locally.
    """
    try:
        local_appt = Appointment.objects.get(id=appointment_id)
        emr_id = local_appt.google_event_id
        
        if emr_id:
            base_url = config('EMR_API_BASE_URL', default='http://localhost:8000/api')
            url = f"{base_url}/appointments/{emr_id}/cancel/"
            response = requests.post(url, headers=get_emr_headers())
            
            # If 400 or 404, it might already be cancelled or not exist, we proceed to delete locally
            if response.status_code not in [200, 204, 400, 404]:
                logger.error(f"Error cancelling in EMR: HTTP {response.status_code}")
                return False
                
        # Delete from local DB so it disappears from the DrME UI
        local_appt.delete()
        return True
        
    except Appointment.DoesNotExist:
        return False
    except Exception as e:
        logger.error(f"An error occurred during cancellation: {e}")
        return False

def get_available_slots(date_str):
    """
    Fetches available slots for the given date from the EMR.
    """
    base_url = config('EMR_API_BASE_URL', default='http://localhost:8000/api')
    headers = get_emr_headers()
    
    try:
        # 1. Get the primary doctor
        docs_resp = requests.get(f"{base_url}/doctors/", headers=headers)
        docs_resp.raise_for_status()
        doctors = docs_resp.json()
        if not doctors:
             return []
        doctor_id = doctors[0]['id']
        
        # 2. Fetch available online slots
        url = f"{base_url}/appointments/available-slots/?doctor_id={doctor_id}&date={date_str}&online_only=true"
        slots_resp = requests.get(url, headers=headers)
        slots_resp.raise_for_status()
        
        return slots_resp.json()
    except Exception as e:
        logger.error(f"Error fetching available slots: {e}")
        return []


def get_available_days_map(days_ahead=42):
    """
    Returns a dict mapping date strings (YYYY-MM-DD) to slot counts
    for the next `days_ahead` days, based on active online schedules.
    Makes a single call to the EMR schedules endpoint — fast.
    """
    from datetime import date, timedelta

    base_url = config('EMR_API_BASE_URL', default='http://localhost:8000/api')
    headers = get_emr_headers()

    try:
        # 1. Get primary doctor
        docs_resp = requests.get(f"{base_url}/doctors/", headers=headers)
        docs_resp.raise_for_status()
        doctors = docs_resp.json()
        if not doctors:
            return {}
        doctor_id = doctors[0]['id']

        # 2. Get all active online schedules for this doctor
        sched_resp = requests.get(
            f"{base_url}/schedules/?doctor_id={doctor_id}",
            headers=headers
        )
        sched_resp.raise_for_status()
        schedules = sched_resp.json()

        # Build set of weekdays (0=Mon…6=Sun) that have online slots
        online_weekdays = {
            s['day_of_week']
            for s in schedules
            if s.get('is_online_allowed') and s.get('is_active', True)
        }

        # 3. Walk the next `days_ahead` days and mark available ones
        availability = {}
        today = date.today()
        for i in range(days_ahead):
            d = today + timedelta(days=i)
            if d.weekday() in online_weekdays:
                # Rough slot count from schedule duration
                day_slots = [
                    s for s in schedules
                    if s['day_of_week'] == d.weekday()
                    and s.get('is_online_allowed')
                    and s.get('is_active', True)
                ]
                # Estimate slots (don't call per-day endpoint here)
                slot_count = sum(
                    max(0, (
                        int(s['end_time'][:2]) * 60 + int(s['end_time'][3:5])
                        - int(s['start_time'][:2]) * 60 - int(s['start_time'][3:5])
                    ) // s.get('slot_duration', 15))
                    for s in day_slots
                )
                availability[d.strftime('%Y-%m-%d')] = slot_count

        return availability

    except Exception as e:
        logger.error(f"Error fetching available days map: {e}")
        return {}

def book_appointment(user_info, date_str, start_time_str, end_time_str):
    """
    Books an appointment in the EMR API.
    Returns True on success, or an error string describing the failure.
    """
    base_url = config('EMR_API_BASE_URL', default='http://localhost:8000/api')
    headers = get_emr_headers()
    user_email = user_info.get("email")
    first_name = user_info.get("given_name", user_info.get("name", "Unknown"))
    last_name = user_info.get("family_name", "")

    try:
        # 1. Get or Create Patient
        patient_resp = requests.get(f"{base_url}/patients/?email={user_email}", headers=headers)
        patient_resp.raise_for_status()
        patients = patient_resp.json()

        if patients:
            patient_id = patients[0]['id']
        else:
            # Create new patient
            new_pat_resp = requests.post(
                f"{base_url}/patients/",
                headers=headers,
                json={
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": user_email,
                    "clinic": 1
                }
            )
            if not new_pat_resp.ok:
                err = new_pat_resp.text[:200]
                logger.error(f"Failed to create patient in EMR: {err}")
                return f"No se pudo registrar el paciente en el sistema ({new_pat_resp.status_code}): {err}"
            patient_id = new_pat_resp.json()['id']

        # 2. Get the primary doctor (first active doctor in clinic 1)
        docs_resp = requests.get(f"{base_url}/doctors/", headers=headers)
        docs_resp.raise_for_status()
        doctors = docs_resp.json()
        if not doctors:
            return "No hay médicos disponibles en el sistema."
        doctor_id = doctors[0]['id']

        # 3. Create Appointment
        appt_resp = requests.post(
            f"{base_url}/appointments/",
            headers=headers,
            json={
                "clinic": 1,
                "patient_id": patient_id,
                "doctor": doctor_id,
                "date": date_str,
                "start_time": start_time_str,
                "end_time": end_time_str,
                "status": "SCHEDULED",
                "is_online_booking": True,
            }
        )
        if not appt_resp.ok:
            err = appt_resp.text[:300]
            logger.error(f"EMR rejected appointment creation ({appt_resp.status_code}): {err}")
            return f"El sistema rechazó la reserva ({appt_resp.status_code}): {err}"

        # Sync the new appointment down to local DB immediately
        fetch_appointments(user_email)
        return True

    except requests.exceptions.ConnectionError:
        logger.error("Could not connect to EMR API")
        return "No se pudo conectar al sistema de turnos. Intentá de nuevo en unos minutos."
    except Exception as e:
        logger.error(f"Error booking appointment: {e}")
        return "Ocurrió un error inesperado al reservar. Por favor intentá de nuevo."


def sync_user_appointments(user_email):
    """
    Syncs appointments from the EMR for a given user and returns a
    structured result dict for use in async API responses.
    Returns: {'synced': int, 'error': str|None}
    """
    try:
        appointments = fetch_appointments(user_email)
        return {'synced': len(appointments), 'error': None}
    except Exception as e:
        logger.error(f"sync_user_appointments failed: {e}")
        return {'synced': 0, 'error': str(e)}
