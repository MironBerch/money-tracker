from datetime import date

from django.test import TestCase
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from categories.models import Category
from transactions.models import Transaction


class TransactionModelTests(TestCase):

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
        Transaction.objects.create(
            user=User.objects.first(),
            amount=100.0,
            name='name',
            category=Category.objects.first(),
            transaction_date=date.today(),
        )

    def test_model_verbose_name_single(self):
        """Test that model verbose name is set correctly."""
        self.assertEqual(Transaction._meta.verbose_name, _('transaction'))

    def test_model_verbose_name_plural(self):
        """Test that model verbose name (in plural) is set correctly."""
        self.assertEqual(Transaction._meta.verbose_name_plural, _('transactions'))

    def test_user_field_params(self):
        """Test that user field has all required parameters."""
        user_field = Transaction._meta.get_field('user')

        self.assertEqual(user_field.verbose_name, _('transaction author'))

    def test_name_field_params(self):
        """Test that name field has all required parameters."""
        name_field = Transaction._meta.get_field('name')

        self.assertEqual(name_field.verbose_name, _('transaction name'))
        self.assertEqual(name_field.max_length, 50)

    def test_description_field_params(self):
        """Test that description field has all required parameters."""
        description_field = Transaction._meta.get_field('description')

        self.assertEqual(description_field.verbose_name, _('transaction description'))
        self.assertEqual(description_field.max_length, 500)

    def test_object_name_has_user_object_name(self):
        """Test that Transaction object name is set up properly."""
        test_transaction: Transaction = Transaction.objects.first()
        self.assertEqual(str(test_transaction), f'{test_transaction.name}')
