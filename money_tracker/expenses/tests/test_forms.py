from django.test import TestCase

from accounts.models import User
from categories.models import Category
from expenses.forms import ExpenseForm


class ExpenseFormTests(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email='testuser@gmail.com',
            first_name='testuser',
            last_name='testuser',
            password='testpass',
        )
        self.category = Category.objects.create(
            user=self.user,
            name='Test Category',
            slug='test-category',
        )

    def test_valid_form(self):
        """Test that form with correct data is valid."""
        form_data = {
            'user': self.user,
            'amount': 100.00,
            'name': 'Test Transaction',
            'description': 'Test Description',
            'category': self.category,
            'expense_date': '2022-01-01',
        }
        form = ExpenseForm(
            user=self.user,
            data=form_data,
        )
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test that form with incorrect data is not valid."""
        form_data = {
            'user': self.user,
            'amount': -50.00,
            'name': '',
            'category': self.category,
            'expense_date': '2022-01-01',
        }
        form = ExpenseForm(
            user=self.user,
            data=form_data,
        )
        self.assertFalse(form.is_valid())
