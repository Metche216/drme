from django.db import models

# Create your models here.

class Testimonio(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'Testimonio de {self.nombre}'