from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterTestCase(APITestCase):       
    def test_register(self):
        data = {
            'username': 'testcase',
            'email': 'admin@admin.com',
            'password': 'admin',
            'password2': 'admin'
        }
        response = self.client.post(reverse('register'),data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

      
class LoginLogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example', password="NewPassword@123")
        
    def test_login(self):
        data = {
            "username": 'example',
            "password": 'NewPassword@123'
        }
        response = self.client.post(reverse('token_obtain_pair'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
        
    