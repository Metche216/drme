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

    name = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'Testimonio de {self.nombre}'


class Appointment(models.Model):
    """ Model representing an appointment """
    start = models.DateTimeField()
    end = models.DateTimeField()
    patient = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    google_event_id = models.CharField(max_length=255, blank=True, null=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Appointment with {self.patient} on {self.start}'


