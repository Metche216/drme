from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime, timedelta



class User(AbstractUser):
    """ Custom user model """
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def set_default_username(self):
        """ Set default username to email """
        if not self.username:
            self.username = self.email
            self.save()
class Testimonio(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(default=5)
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'Testimonio de {self.name}'


class Appointment(models.Model):
    """ Model representing an appointment """
    start = models.DateTimeField()
    end = models.DateTimeField()
    patient = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=20, blank=True, default='')
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    google_event_id = models.CharField(max_length=255, blank=True, null=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Appointment with {self.patient} on {self.start}'


class PatientProfile(models.Model):
    """
    Stores the patient's confirmed personal data for online booking.
    Keyed by email (from Auth0 session) — works with any Auth0 login method.
    Created the first time a user completes the profile form before booking.
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} <{self.email}>'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()
