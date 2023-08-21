from django.test import TestCase
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from transactions.models import Category


class CategoryModelTests(TestCase):

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

    def test_model_verbose_name_single(self):
        """Test that model verbose name is set correctly."""
        self.assertEqual(Category._meta.verbose_name, _('category'))

    def test_model_verbose_name_plural(self):
        """Test that model verbose name (in plural) is set correctly."""
        self.assertEqual(Category._meta.verbose_name_plural, _('categories'))

    def test_user_field_params(self):
        """Test that user field has all required parameters."""
        user_field = Category._meta.get_field('user')

        self.assertEqual(user_field.verbose_name, _('category author'))

    def test_name_field_params(self):
        """Test that name field has all required parameters."""
        name_field = Category._meta.get_field('name')

        self.assertEqual(name_field.verbose_name, _('name of category'))
        self.assertEqual(name_field.max_length, 50)

    def test_slug_field_params(self):
        """Test that slug field has all required parameters."""
        last_name_field = Category._meta.get_field('slug')

        self.assertEqual(last_name_field.verbose_name, _('slug for category'))
        self.assertEqual(last_name_field.max_length, 50)

    def test_object_name_has_user_object_name(self):
        """Test that Category object name is set up properly."""
        test_category: Category = Category.objects.first()
        self.assertEqual(str(test_category), f'{test_category.name}')
