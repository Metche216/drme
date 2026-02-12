from django.core.management.base import BaseCommand
from core.models import Appointment

class Command(BaseCommand):
    help = 'Fix appointments that have the doctor email instead of patient email'

    def add_arguments(self, parser):
        parser.add_argument(
            '--patient-email',
            type=str,
            help='The correct patient email to use',
            required=True
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be updated without making changes',
        )

    def handle(self, *args, **options):
        patient_email = options['patient_email']
        dry_run = options['dry_run']

        # Find all appointments with doctor's email
        doctor_email = "drmatiasetcheverry@gmail.com"
        appointments = Appointment.objects.filter(email=doctor_email)

        self.stdout.write(f"Found {appointments.count()} appointments with doctor's email")

        if dry_run:
            self.stdout.write(self.style.WARNING("DRY RUN - No changes will be made"))
            for appt in appointments:
                self.stdout.write(f"  Would update: ID={appt.id}, Patient={appt.patient}, Start={appt.start}")
        else:
            updated = appointments.update(email=patient_email)
            self.stdout.write(self.style.SUCCESS(f"Updated {updated} appointments to use email: {patient_email}"))
