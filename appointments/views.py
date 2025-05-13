from django.shortcuts import render
from django.http import JsonResponse
import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from decouple import config

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

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
        print("Fetching the next 10 events from the calendar...")

        events_result = service.events().list(
            calendarId="primary",  # Use "primary" for the default calendar or specify a calendar ID
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        ).execute()

        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
            return []

        # Return the events as a list of dictionaries
        return [
            {"start": event["start"].get("dateTime", event["start"].get("date")), "summary": event["summary"]}
            for event in events
        ]

    except HttpError as error:
        print(f"An error occurred: {error}")
        return []

def api_fetch_appointments(request):
    """
    API endpoint to fetch appointments.
    Returns a JSON response with the events.
    """
    appointments = fetch_appointments()  # Fetch events synchronously
    return JsonResponse({"appointments": appointments})

def list_appointments(request):
    """
    View to render the appointments page.
    """
    return render(request, "appointments/appointments.html")