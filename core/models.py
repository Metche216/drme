from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



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

