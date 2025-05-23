from django.test import TestCase
from django.urls import reverse

from core.models import Testimonio, User, Appointment
from django.contrib.auth import get_user_model

class ModelTestSuite(TestCase):
    def test_create_new_testimonio(self):
        """ Test creating a new Testimonio instance """
        testimonio = Testimonio.objects.create(
            name="John Doe",
            content="This is a testimonio.",
            date="2023-10-01"
        )
        all_testimonios = Testimonio.objects.all()
        self.assertEqual(all_testimonios.count(), 1)
        self.assertEqual(all_testimonios[0].name, "John Doe")

    def test_create_new_user(self):
        """ Test creating a new user instance """
        user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="useremail@example.com",
            )
        all_users = User.objects.all()
        self.assertEqual(all_users.count(), 1)
        self.assertEqual(all_users[0].username, "testuser")

    def test_create_blank_appointments(self):
        appointment = Appointment.objects.create(
            start="2023-10-01T10:00:00Z",
            end="2023-10-01T11:00:00Z",
            patient="John Doe",
            cellphone="1234567890",
            email="jd@example.com",
        )
        all_appointments = Appointment.objects.all()
        self.assertEqual(all_appointments.count(), 1)
        self.assertEqual(all_appointments[0].patient, "John Doe")