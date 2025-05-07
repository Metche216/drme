from django.test import TestCase
from django.urls import reverse

from core.models import Testimonio

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

