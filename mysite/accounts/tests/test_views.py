from django.test import TestCase,Client
from django.urls import reverse
import json
from accounts.models import Student


class TestViews(TestCase):

    def test_student_view(self):

        client = Client()
        response = client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'register.html')


    def test_edit_profile_view(self):

        client = Client()
        response = client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'register.html')
