from django.test import TestCase
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from budgets.models import Budget


class BudgetModelTests(TestCase):

    def setUp(self) -> None:
        User.objects.create_user(
            email='user1@gmail.com',
            first_name='John',
            last_name='Doe',
            password='password',
        )

    def test_model_verbose_name_single(self):
        """Test that model verbose name is set correctly."""
        self.assertEqual(Budget._meta.verbose_name, _('budget'))

    def test_model_verbose_name_plural(self):
        """Test that model verbose name (in plural) is set correctly."""
        self.assertEqual(Budget._meta.verbose_name_plural, _('budgets'))

    def test_budget_field_params(self):
        """Test that budget field has all required parameters."""
        budget_field = Budget._meta.get_field('budget')

        self.assertEqual(budget_field.verbose_name, _('overall budget'))
        self.assertEqual(budget_field.default, 0)

    def test_object_name_has_user_object_name(self):
        """Test that budget object name is set up properly."""
        test_budget: Budget = Budget.objects.first()
        self.assertEqual(str(test_budget), f'{test_budget.budget}')
