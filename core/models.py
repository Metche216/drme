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

    def __str__(self):
        return f'Appointment with {self.patient} on {self.start}'

    def create_new_blank_appointments(self, interval):
        """ Create a new blank appointment """

        start_time = datetime.now() + timedelta(days=5)
        start_hour = start_time.replace(hour=8, minute=0, second=0)
        end_hour = start_time.replace(hour=11, minute=40, second=0)
        delta=timedelta(minutes=interval)

        current = start_hour
        while current < end_hour:
            yield current
            current += delta
            try:
                Appointment.objects.get(start=current)
            except Appointment.DoesNotExist:
                Appointment.objects.create(
                    start=current,
                    end=current + timedelta(minutes=interval),
                    patient="",
                    cellphone="",
                    email="",
                )
                print(f"Created appointment from {current} to {current + timedelta(minutes=interval)}")
