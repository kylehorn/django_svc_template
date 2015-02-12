import unittest
from .models import UserProfile
from django.contrib.auth.models import User
from django.test.utils import override_settings
from rest_framework import status
from rest_framework.test import APITestCase


class UserProfileTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(
            'testuser', 'user@test.com', 'password')
        cls.user.save()
        cls.profile = cls.user.profile

    def test_create_profile(self):
        """Saving a User object should create a UserProfile"""
        self.assertIsInstance(self.user.profile, UserProfile)

    def test_profile_unicode(self):
        """UserProfile should have a string representation"""
        self.assertEqual(
            unicode(self.profile), self.profile.user.username)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()


@override_settings(REST_FRAMEWORK={
    'EXCEPTION_HANDLER': '{{cookiecutter.repo_name}}.exceptions.application_exception_handler',
    'PAGINATE_BY': 100,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
})
class AccountTests(APITestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(
            'testuser', 'user@test.com', 'password')
        cls.user.save()

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def test_signup(self):
        """Ensure we can signup"""
        data = {'username': 'newtestuser',
                'password': 'password'}
        response = self.client.post('/api/v1/signup/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertTrue(response.data['is_active'])

    def test_signup_username_exists(self):
        """Ensure we cannot signup with duplicate username"""
        data = {'username': 'testuser',
                'password': 'password'}
        response = self.client.post('/api/v1/signup/', data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_self_pk(self):
        """Ensure we can pass self instead of pk"""
        response = self.client.get('/api/v1/users/self/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
