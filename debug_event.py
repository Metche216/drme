from datetime import datetime, timedelta
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from decouple import config
import json

SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Load credentials
service_account_file = config("GOOGLE_SERVICE_ACCOUNT_FILE")
creds = Credentials.from_service_account_file(service_account_file, scopes=SCOPES)
service = build("calendar", "v3", credentials=creds)

# Fetch a specific event
event_id = "7rgisi44u9n6tjronp4ggvvrfs"
event = service.events().get(
    calendarId="drmatiasetcheverry@gmail.com",
    eventId=event_id
).execute()

print("=" * 80)
print(f"Event ID: {event_id}")
print("=" * 80)
print(json.dumps(event, indent=2, default=str))
