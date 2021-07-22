from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """
        Test creatign a new user with an email is successful
        """
        email = 'krnadiger@gmail.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test email normalization"""
        email = "krnadiger@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(email.lower(), user.email)

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_super_user_creating_using_cli(self):
        """Test creating new super user"""
        user = get_user_model().objects.create_superuser(
            'krnadiger@gmail.com',
            'password123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
