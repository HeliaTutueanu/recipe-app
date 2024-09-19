from django.test import TestCase, Client
from .models import CustomUser
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import User

class UserModelTest(TestCase):
    def setUpTestData():
        user = User.objects.create_user(username='davidsgoggins', password='testpassword')
        CustomUser.objects.create(user=user, name='David Goggins')
        
    def test_user_name(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_user_name_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEqual(max_length, 120, 'name has over 120 characters')

    def test_user_username_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user.user._meta.get_field('username').max_length
        self.assertEqual(max_length, 150, 'username has over 120 characters')

class UserAuthTest(TestCase):
    def setUpTestData():
        Client()
        user = User.objects.create_user(username='testuser', password='testpassword')
        CustomUser.objects.create(
            user = user,
            name='testcustomuser'
        )