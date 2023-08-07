from django.test import TestCase

from accounts.models import User
from accounts.services import get_user_by_email, get_user_by_pk


class AccountsServicesTests(TestCase):

    def setUp(self) -> None:
        User.objects.create_user(
            email='user@gmail.com',
            first_name='John',
            last_name='Doe',
            password='password',
        )

    def test_get_user_by_pk(self):
        """Test that get_user_by_pk method works correctly with `int` and `str` pk."""
        self.assertEqual(get_user_by_pk(pk=User.objects.first().id), User.objects.first())
        self.assertEqual(get_user_by_pk(pk=str(User.objects.first().id)), User.objects.first())

    def test_get_user_by_email(self):
        """Test that get_user_by_email method works correctly."""
        self.assertEqual(get_user_by_email(email='user@gmail.com'), User.objects.first())
