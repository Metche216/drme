from datetime import datetime, timedelta
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from decouple import config
from core.models import Appointment, User
import re

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def fetch_appointments():
    """
    Fetches events from Google Calendar and syncs them to the local database.
    Returns a list of synced Appointment objects.
    """
    print("Fetching appointments from Google Calendar...")
    try:
        # Load the service account file path from the .env file
        service_account_file = config("GOOGLE_SERVICE_ACCOUNT_FILE")
        creds = Credentials.from_service_account_file(service_account_file, scopes=SCOPES)

        # Build the Google Calendar API service
        service = build("calendar", "v3", credentials=creds)

        time_min = datetime.utcnow().isoformat() + 'Z'  # now
        time_max = (datetime.utcnow() + timedelta(days=90)).isoformat() + 'Z' # 3 months out

        print(f"Time Range: {time_min} to {time_max}")
        log_debug(f"Fetching appointments from GCal. Range: {time_min} to {time_max}")

        events_result = service.events().list(
            calendarId="drmatiasetcheverry@gmail.com",
            timeMin=time_min,
            timeMax=time_max,
            maxResults=50,
            singleEvents=True,
            orderBy="startTime",
        ).execute()

        events = events_result.get("items", [])
        print(f"Found {len(events)} events.")
        log_debug(f"Found {len(events)} events in GCal.")

        if not events:
            # Debug: Print the raw result to see if anything else came back
            print(f"Raw Result Keys: {events_result.keys()}")
            print("No upcoming events found.")
            return []

        synced_appointments = []

        for event in events:
            # GCal Booking slots usually have the user as an attendee or in the description
            # But the most reliable way for GCal Appointment Scheduling is checking attendees
            attendees = event.get('attendees', [])

            # Find the attendee that is NOT the organizer (the doctor)
            patient_email = None
            patient_name = "Unknown"

            for attendee in attendees:
                if attendee.get('email') != "drmatiasetcheverry@gmail.com":
                    patient_email = attendee.get('email')
                    patient_name = attendee.get('displayName', patient_email.split('@')[0])
                    break

            # Fallback: check description for email (GCal Appointment Slots often put it there)
            if not patient_email and event.get('description'):
                description = event.get('description')
                # Try to find email pattern in description
                # Adjusted regex to be a bit more permissible for GCal's formatting
                # Find ALL matches, not just the first one
                email_matches = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', description)

                for email in email_matches:
                    if email.lower() != "drmatiasetcheverry@gmail.com":
                        patient_email = email
                        break

                if patient_email:
                    # Try to extract name? Usually "Reservada por [Name]"
                    # Spanish: "Reservada por" -> Reserved by
                    name_match = re.search(r'Reservada por\s+(.*?)(?:<br>|\n|$)', description)
                    if name_match:
                         # Remove HTML tags if present
                        raw_name = name_match.group(1)
                        patient_name = re.sub(r'<[^>]+>', '', raw_name).strip()
                    else:
                        # Fallback for name if we have email
                        patient_name = patient_email.split('@')[0]

            if not patient_email:
                print("  No patient email found in attendees or description. Skipping.")
                log_debug(f"Skipping event {event['id']}: No patient email found.")
                continue

            start = event["start"].get("dateTime")
            end = event["end"].get("dateTime")
            event_id = event["id"]

            # Try to find user by email
            user = User.objects.filter(email=patient_email).first()

            log_debug(f"Syncing event {event_id}. Patient: {patient_email}. User found? {user is not None}")

            appointment, created = Appointment.objects.update_or_create(
                google_event_id=event_id,
                defaults={
                    "start": start,
                    "end": end,
                    "patient": patient_name,
                    "email": patient_email,
                    "cellphone": "",
                    "user": user
                }
            )

            if created:
                print(f"Created/Synced appointment for {patient_email}")
                log_debug(f"Created new appointment for {patient_email}")

            synced_appointments.append(appointment)

        return synced_appointments

    except HttpError as error:
        print(f"An error occurred: {error}")
        log_debug(f"HttpError in fetch_appointments: {error}")
        return []

def log_debug(message):
    try:
         with open("d:\\Programming\\DrME\\debug.log", "a") as f:
            f.write(f"SERVICE {datetime.now()}: {message}\n")
    except Exception as e:
        print(f"Logging failed: {e}")

def cancel_appointment_service(appointment_id):
    log_debug(f"Attempting to cancel appointment {appointment_id}")
    """
    Cancels an appointment by deleting it from Google Calendar and the local database.
    Returns True if successful, False otherwise.
    """
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        google_event_id = appointment.google_event_id

        if google_event_id:
            # Load credentials
            service_account_file = config("GOOGLE_SERVICE_ACCOUNT_FILE")
            creds = Credentials.from_service_account_file(service_account_file, scopes=SCOPES)
            service = build("calendar", "v3", credentials=creds)

            # Delete from Google Calendar
            try:
                service.events().delete(
                    calendarId="drmatiasetcheverry@gmail.com",
                    eventId=google_event_id
                ).execute()
                print(f"Deleted event {google_event_id} from Google Calendar.")
                log_debug(f"Successfully deleted event {google_event_id} from GCal")
            except HttpError as error:
                # If 410 (Gone) or 404 (Not Found), it's already deleted, so proceed to delete local
                if error.resp.status in [404, 410]:
                    print(f"Event {google_event_id} already deleted from GCal.")
                else:
                    print(f"Error deleting from GCal: {error}")
                    log_debug(f"Error deleting from GCal: {error}")
                    return False

        # Delete from local DB
        appointment.delete()
        print(f"Deleted appointment {appointment_id} from local DB.")
        log_debug(f"Deleted appointment {appointment_id} from local DB")
        return True

    except Appointment.DoesNotExist:
        print(f"Appointment {appointment_id} not found.")
        return False
    except Exception as e:
        print(f"An error occurred during cancellation: {e}")
        log_debug(f"Generic error during cancellation: {e}")
        return False
