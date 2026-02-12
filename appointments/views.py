from django.shortcuts import render, redirect
from django.http import JsonResponse

from core.models import Appointment, User
from .services import fetch_appointments, cancel_appointment_service


def api_fetch_appointments(request):
#     print("API endpoint called")
#     appointments = fetch_appointments()
    return JsonResponse({"appointments": ''})

def list_appointments(request):
    """
    View to render the appointments page.
    """
    user_session = request.session.get("user")

    if not user_session:
        return redirect("login")

    # Sync appointments from Google Calendar (Temporary: usually done via background task)
    fetch_appointments()

    user_email = user_session.get("userinfo", {}).get("email")
    appointments = Appointment.objects.filter(email=user_email).order_by('-start')

    # Extract user info for pre-filling GCal iframe
    user_info = user_session.get("userinfo", {})
    context = {
        "appointments": appointments,
        "user_name": user_info.get("name", ""),
        "user_email": user_info.get("email", ""),
        "session": user_session # Pass session for base template auth check
    }

    return render(request, "appointments/appointments.html", context)

from datetime import datetime
def log_debug_view(message):
    try:
         with open("d:\\Programming\\DrME\\debug.log", "a") as f:
            f.write(f"VIEW {datetime.now()}: {message}\n")
    except Exception as e:
        print(f"Logging failed: {e}")

def cancel_appointment(request, appointment_id):
    """
    View to cancel an appointment.
    """
    if request.method == "POST":
        user_session = request.session.get("user")
        if not user_session:
             return redirect("login")

        # Verify ownership (optional but recommended)
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            user_email = user_session.get("userinfo", {}).get("email")

            log_debug_view(f"Request to cancel {appointment_id} by {user_email}. Appt email: {appointment.email}")

            if appointment.email != user_email:
                 # Simple authorization check
                 log_debug_view(f"Optimization check failed: {appointment.email} != {user_email}")
                 return redirect("list_appointments")

            success = cancel_appointment_service(appointment_id)
            if success:
                print(f"Appointment {appointment_id} cancelled successfully.")
                log_debug_view(f"Appointment {appointment_id} cancelled successfully.")
            else:
                print(f"Failed to cancel appointment {appointment_id}.")
                log_debug_view(f"Failed to cancel appointment {appointment_id}.")

        except Appointment.DoesNotExist:
            log_debug_view(f"Appointment {appointment_id} does not exist in View.")
            pass

        return redirect("list_appointments")

    return redirect("list_appointments")