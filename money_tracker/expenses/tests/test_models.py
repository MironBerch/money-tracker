from datetime import date

from django.test import TestCase
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from categories.models import Category
from expenses.models import Expense


class ExpenseModelTests(TestCase):

    def setUp(self) -> None:
        User.objects.create_user(
            email='user1@gmail.com',
            first_name='John',
            last_name='Doe',
            password='password',
        )
        Category.objects.create(
            user=User.objects.first(),
            name='fst category',
            slug='fst-category',
        )
        Expense.objects.create(
            user=User.objects.first(),
            amount=100.0,
            name='name',
            category=Category.objects.first(),
            expense_date=date.today(),
        )

    def test_model_verbose_name_single(self):
        """Test that model verbose name is set correctly."""
        self.assertEqual(Expense._meta.verbose_name, _('expense'))

    def test_model_verbose_name_plural(self):
        """Test that model verbose name (in plural) is set correctly."""
        self.assertEqual(Expense._meta.verbose_name_plural, _('expenses'))

    def test_user_field_params(self):
        """Test that user field has all required parameters."""
        user_field = Expense._meta.get_field('user')

        self.assertEqual(user_field.verbose_name, _('expense author'))

    def test_name_field_params(self):
        """Test that name field has all required parameters."""
        name_field = Expense._meta.get_field('name')

        self.assertEqual(name_field.verbose_name, _('expense name'))
        self.assertEqual(name_field.max_length, 50)

    def test_description_field_params(self):
        """Test that description field has all required parameters."""
        description_field = Expense._meta.get_field('description')

        self.assertEqual(description_field.verbose_name, _('expense description'))
        self.assertEqual(description_field.max_length, 500)

    def test_object_name_has_user_object_name(self):
        """Test that Expense object name is set up properly."""
        test_expense: Expense = Expense.objects.first()
        self.assertEqual(str(test_expense), f'{test_expense.name}')
