from django.test import TestCase

from accounts.models import Profile, User


class AccountsSignalsTests(TestCase):

    def setUp(self) -> None:
        User.objects.create_user(
            email='user@gmail.com',
            first_name='John',
            last_name='Doe',
            password='Password',
        )
        User.objects.create_staffuser(
            email='staffuser@gmail.com',
            first_name='Bill',
            last_name='White',
            password='Password',
        )
        User.objects.create_superuser(
            email='superuser@gmail.com',
            first_name='Bill',
            last_name='White',
            password='Password',
        )

    def test_user_profile_attribute(self):
        """Test that user model has profile attribute."""
        self.assertTrue(hasattr(User.objects.first(), 'profile'))
        self.assertEqual(User.objects.first().profile.user, User.objects.first())

    def test_create_user_profile_signal(self):
        """Test that create_user_profile signal works with new users."""
        self.assertTrue(Profile.objects.get(user=User.objects.get(email='user@gmail.com')))

    def test_create_staffuser_profile_signal(self):
        """Test that create_user_profile signal works with new staffuser."""
        self.assertTrue(Profile.objects.get(user=User.objects.get(email='staffuser@gmail.com')))

    def test_create_superuser_profile_signal(self):
        """Test that create_user_profile signal works with new superusers."""
        self.assertTrue(Profile.objects.get(user=User.objects.get(email='superuser@gmail.com')))
