from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class PublicPagesTests(TestCase):
    """ Test the public pages """
    def test_index_page(self):
        """ Test the index page """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class PrivatePagesTests(TestCase):
    """ Test the private pages """

    def setUp(self):
        """ Create a user and log in """
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

