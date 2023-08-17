from django.test import TestCase

from accounts.models import User
from categories.forms import CategoryForm
from categories.models import Category


class CategoryFormTests(TestCase):

    def setUp(self):
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

    def test_category_form_valid(self):
        """Test that form with correct data is valid."""
        form_data = {
            'name': 'New Category',
        }
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_category_form_invalid(self):
        """Test that form with incorrect data is not valid."""
        form_data = {
            'name': '',
        }
        form = CategoryForm(data=form_data)
        self.assertFalse(form.is_valid())
