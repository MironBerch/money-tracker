from django.test import TestCase

from accounts.models import User


class UserManagerTests(TestCase):

    def test_create_user(self):
        """Test creating a regular user."""
        email = 'user@example.com'
        password = 'password'
        first_name = 'John'
        last_name = 'Doe'

        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_staffuser(self):
        """Test creating a staff user."""
        email = 'staff@example.com'
        password = 'password'
        first_name = 'Jane'
        last_name = 'Smith'

        user = User.objects.create_staffuser(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertTrue(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Test creating a superuser."""
        email = 'admin@example.com'
        password = 'password'
        first_name = 'Admin'
        last_name = 'User'

        user = User.objects.create_superuser(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
