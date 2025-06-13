from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from decouple import config

from core.models import Appointment
from core.utils import create_new_blank_appointments

import re

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def fetch_appointments():
    """
    Fetches the next 10 events from the centralized Google Calendar.
    Returns a list of dictionaries containing event details.
    """
    print("Fetching appointments from Google Calendar...")
    try:
        # Load the service account file path from the .env file
        service_account_file = config("GOOGLE_SERVICE_ACCOUNT_FILE")
        creds = Credentials.from_service_account_file(service_account_file, scopes=SCOPES)

        # Build the Google Calendar API service
        service = build("calendar", "v3", credentials=creds)

        print("Fetching the next 10 events from the calendar...")
        time_min = datetime.utcnow().isoformat() + 'Z'  # ahora
        time_max = (datetime.utcnow() + timedelta(days=30)).isoformat() + 'Z'

        calendar_list = service.calendarList().list().execute()

        events_result = service.events().list(
            calendarId="drmatiasetcheverry@gmail.com",
            timeMin=time_min,
            timeMax=time_max,
            maxResults=50,
            singleEvents=True,
            orderBy="startTime",
        ).execute()

        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
            return []
        else:
            for event in events:
                start = event["start"].get("dateTime")
                end = event["end"].get("dateTime")
                patient_data = re.split(r"\n", event['description'])
                patient = patient_data[1]
                email = patient_data[2]
                cellphone = patient_data[3]
                appointment, created = Appointment.objects.get_or_create(

                    email=email,
                    defaults={
                        "patient": patient,
                        "cellphone": cellphone,
                        "start":start,
                        "end":end,
                    }
                )

                if created:
                    print(f"Created new appointment for {email}")


        all_appointments = Appointment.objects.all()

        return [
            {
                start: appointment.start,
                end: appointment.end,
                patient: appointment.patient,
                cellphone: appointment.cellphone,
                email: appointment.email,
            }
            for appointment in all_appointments
        ]

    except HttpError as error:
        print(f"An error occurred: {error}")
        return []

def api_fetch_appointments(request):
#     print("API endpoint called")
#     appointments = fetch_appointments()
    return JsonResponse({"appointments": ''})

def list_appointments(request):
    """
    View to render the appointments page.
    """

    appointments = Appointment.objects.all()  # Fetch all appointments from the database
    return render(request, "appointments/appointments.html", {"appointments": appointments})