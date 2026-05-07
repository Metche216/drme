import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from core.models import Appointment, PatientProfile
from .services import fetch_appointments, cancel_appointment_service, get_available_slots, book_appointment, sync_user_appointments
from datetime import datetime

import logging
logger = logging.getLogger(__name__)


def _get_session_user(request):
    """Returns the session user dict or None."""
    return request.session.get("user")

def list_appointments(request):
    """
    View to render the appointments page.
    Does NOT sync from EMR synchronously — sync is triggered async from the frontend.
    """
    user_session = request.session.get("user")

    if not user_session:
        return redirect("login")

    user_email = user_session.get("userinfo", {}).get("email")

    # Read only from local DB — frontend will trigger async sync separately
    appointments = Appointment.objects.filter(email=user_email).order_by('-start')

    user_info = user_session.get("userinfo", {})
    context = {
        "appointments": appointments,
        "user_name": user_info.get("name", ""),
        "user_email": user_email,
        "session": user_session
    }

    return render(request, "appointments/appointments.html", context)


@require_http_methods(["GET"])
def api_sync_appointments(request):
    """
    Async-friendly JSON endpoint that triggers an EMR sync for the current user.
    Called by the frontend on page load; returns the number of synced appointments.
    """
    user_session = request.session.get("user")
    if not user_session:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    user_email = user_session.get("userinfo", {}).get("email")
    result = sync_user_appointments(user_email)
    return JsonResponse(result)


@require_http_methods(["GET"])
def api_available_slots(request):
    """
    JSON endpoint for the frontend wizard to fetch available slots.
    Requires an active session. Expects ?date=YYYY-MM-DD
    """
    user_session = request.session.get("user")
    if not user_session:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    date_str = request.GET.get('date')
    if not date_str:
        return JsonResponse({'error': 'date parameter is required'}, status=400)

    slots = get_available_slots(date_str)
    return JsonResponse({'slots': slots})


@require_http_methods(["POST"])
def api_save_profile(request):
    """
    Saves (or updates) the patient's personal profile so future bookings
    don't ask again and the EMR always gets consistent data.
    """
    user_session = request.session.get("user")
    if not user_session:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    try:
        data = json.loads(request.body)
        email = user_session.get("userinfo", {}).get("email")
        first_name = data.get('first_name', '').strip()
        last_name = data.get('last_name', '').strip()
        phone_number = data.get('phone_number', '').strip()

        if not first_name or not last_name:
            return JsonResponse({'error': 'Nombre y apellido son obligatorios.'}, status=400)

        profile, _ = PatientProfile.objects.update_or_create(
            email=email,
            defaults={
                'first_name': first_name,
                'last_name': last_name,
                'phone_number': phone_number,
            }
        )
        return JsonResponse({'status': 'saved'})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)


@require_http_methods(["POST"])
def api_book_appointment(request):
    """
    Books an appointment. If the user has no saved PatientProfile, returns
    profile_required with pre-filled Auth0 data so the frontend can prompt them.
    """
    user_session = request.session.get("user")
    if not user_session:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    try:
        data = json.loads(request.body)
        date_str = data.get('date')
        start_time_str = data.get('start_time')
        end_time_str = data.get('end_time')

        if not all([date_str, start_time_str, end_time_str]):
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        user_info = user_session.get("userinfo", {})
        email = user_info.get("email", "")

        # Check if we have a saved patient profile for this user
        profile = PatientProfile.objects.filter(email=email).first()

        if not profile:
            # Return pre-filled data from Auth0 so the user can confirm/correct
            return JsonResponse({
                'status': 'profile_required',
                'prefill': {
                    'first_name': user_info.get('given_name', ''),
                    'last_name': user_info.get('family_name', ''),
                    'email': email,
                    'phone_number': '',
                }
            })

        # Profile exists — use it for booking
        booking_info = {
            'email': email,
            'given_name': profile.first_name,
            'family_name': profile.last_name,
            'phone_number': profile.phone_number,
        }
        result = book_appointment(booking_info, date_str, start_time_str, end_time_str)

        if result is True:
            return JsonResponse({'status': 'success'})
        else:
            error_msg = result if isinstance(result, str) else 'Failed to book appointment in EMR'
            logger.error(f"Booking failed: {error_msg}")
            return JsonResponse({'error': error_msg}, status=500)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)


def cancel_appointment(request, appointment_id):
    """
    View to cancel an appointment.
    """
    if request.method == "POST":
        user_session = request.session.get("user")
        if not user_session:
             return redirect("login")

        try:
            appointment = Appointment.objects.get(id=appointment_id)
            user_email = user_session.get("userinfo", {}).get("email")

            if appointment.email != user_email:
                 # Simple authorization check
                 return redirect("list_appointments")

            success = cancel_appointment_service(appointment_id)
            if success:
                logger.info(f"Appointment {appointment_id} cancelled successfully.")
            else:
                logger.error(f"Failed to cancel appointment {appointment_id}.")

        except Appointment.DoesNotExist:
            logger.error(f"Appointment {appointment_id} does not exist.")

        return redirect("list_appointments")

    return redirect("list_appointments")
