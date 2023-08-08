from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import User


class AccountsViewsTests(TestCase):

    def test_signup_view(self):
        """Test the `SignUpView`."""
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_view_post(self):
        """Test the `SignUpView` POST request."""
        user_count_before = User.objects.count()

        response = self.client.post(reverse('signup'), data={
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'first_name': 'John',
            'last_name': 'Doe',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), user_count_before + 1)
        self.assertRedirects(response, reverse('signin'))

    def test_signin_view(self):
        """Test the `SignInView`."""
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signin.html')

    def test_signout_view(self):
        """Test the SignOutView."""
        response = self.client.get(reverse('signout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signout.html')


class PasswordResetViewTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.reset_url = reverse('password_reset')

    def test_password_reset_view_get(self):
        response = self.client.get(self.reset_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset.html')

    def test_password_reset_view_post(self):
        data = {
            'email': 'test@example.com',
        }
        response = self.client.post(self.reset_url, data)
        self.assertRedirects(response, reverse('password_reset_done'))
