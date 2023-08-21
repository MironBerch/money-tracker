from django.test import TestCase

from accounts.models import User
from budgets.models import Budget


class BudgetSignalsTests(TestCase):

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

    def test_user_budget_attribute(self):
        """Test that user model has budget attribute."""
        self.assertTrue(hasattr(User.objects.first(), 'budget'))
        self.assertEqual(User.objects.first().budget.user, User.objects.first())

    def test_create_user_budget_signal(self):
        """Test that create_user_budget signal works with new users."""
        self.assertTrue(Budget.objects.get(user=User.objects.get(email='user@gmail.com')))

    def test_create_staffuser_budget_signal(self):
        """Test that create_user_budget signal works with new staffuser."""
        self.assertTrue(Budget.objects.get(user=User.objects.get(email='staffuser@gmail.com')))

    def test_create_superuser_budget_signal(self):
        """Test that create_user_budget signal works with new superusers."""
        self.assertTrue(Budget.objects.get(user=User.objects.get(email='superuser@gmail.com')))
