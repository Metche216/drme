from django.core.management.base import BaseCommand
from appointments.services import fetch_appointments

class Command(BaseCommand):
    help = 'Syncs appointments from Google Calendar to the local database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting appointment sync...'))

        synced = fetch_appointments()

        count = len(synced)
        self.stdout.write(self.style.SUCCESS(f'Successfully synced {count} appointments.'))
