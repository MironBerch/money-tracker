from django.test import TestCase
from django.utils.translation import gettext_lazy as _

from accounts.models import (
    Profile,
    ProfileGenderChoices,
    Settings,
    SettingsСurrencyChoices,
    User,
    get_profile_image_upload_path,
)


class UserModelTests(TestCase):

    def setUp(self) -> None:
        User.objects.create_user(
            email='user1@gmail.com',
            first_name='John',
            last_name='Doe',
            password='password',
        )

    def test_model_verbose_name_single(self):
        """Test that model verbose name is set correctly."""
        self.assertEqual(User._meta.verbose_name, _('user'))

    def test_model_verbose_name_plural(self):
        """Test that model verbose name (in plural) is set correctly."""
        self.assertEqual(User._meta.verbose_name_plural, _('users'))

    def test_email_field_params(self):
        """Test that email field has all required parameters."""
        email_field = User._meta.get_field('email')

        self.assertEqual(email_field.verbose_name, _('email address'))
        self.assertEqual(email_field.max_length, 100)
        self.assertTrue(email_field.unique)

    def test_first_name_field_params(self):
        """Test that first_name field has all required parameters."""
        first_name_field = User._meta.get_field('first_name')

        self.assertEqual(first_name_field.verbose_name, _('first name'))
        self.assertEqual(first_name_field.max_length, 40)

    def test_last_name_field_params(self):
        """Test that last_name field has all required parameters."""
        last_name_field = User._meta.get_field('last_name')

        self.assertEqual(last_name_field.verbose_name, _('last name'))
        self.assertEqual(last_name_field.max_length, 40)

    def test_date_joined_field_params(self):
        """Test that date_joined field has all required parameters."""
        date_joined_field = User._meta.get_field('date_joined')

        self.assertEqual(date_joined_field.verbose_name, _('date joined'))
        self.assertTrue(date_joined_field.auto_now_add)

    def test_last_login_field_params(self):
        """Test that last_login field has all required parameters."""
        last_login_field = User._meta.get_field('last_login')

        self.assertEqual(last_login_field.verbose_name, _('last login'))
        self.assertTrue(last_login_field.auto_now)

    def test_is_staff_field_params(self):
        """Test that is_staff field has all required parameters."""
        is_staff_field = User._meta.get_field('is_staff')
        self.assertFalse(is_staff_field.default)

    def test_is_superuser_field_params(self):
        """Test that is_superuser field has all required parameters."""
        is_superuser_field = User._meta.get_field('is_superuser')
        self.assertFalse(is_superuser_field.default)

    def test_is_active_field_params(self):
        """Test that is_active field has all required parameters."""
        is_active_field = User._meta.get_field('is_active')
        self.assertTrue(is_active_field.default)

    def test_object_name_is_email(self):
        """Test that User object name is set up properly."""
        test_user: User = User.objects.first()
        self.assertEqual(str(test_user), str(test_user.email))

    def test_login_parameter_is_email(self):
        """Test that USERNAME_FIELD is set to `email`."""
        self.assertEqual(User.USERNAME_FIELD, 'email')

    def test_required_fields_include_email_and_first_and_last_name(self):
        """Test that `first_name` and `last_name` are in the REQUIRED_FIELDS."""
        self.assertListEqual(User.REQUIRED_FIELDS, ['first_name', 'last_name'])

    def test_create_superuser_updates_admin_related_fields(self):
        """Test that create_superuser() creates new `superuser`."""
        user = User.objects.create_superuser(
            email='staff1@gmail.com',
            first_name='Test',
            last_name='Test',
            password='password',
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_get_or_create_get_existing_user(self):
        """Test that get_or_create() returns User object if it already exists."""
        user, created = User.objects.get_or_create(
            email='user1@gmail.com',
        )

        self.assertEqual(user, User.objects.first())
        self.assertFalse(created)

    def test_get_or_create_create_new_user(self):
        """Test that get_or_create() creates new User object if it doesn't already exist."""
        user, created = User.objects.get_or_create(
            email='new123@gmail.com',
            first_name='John',
            last_name='Doe',
            password='password',
        )

        self.assertNotEqual(user, User.objects.first())
        self.assertEqual(user, User.objects.get(email='new123@gmail.com'))
        self.assertTrue(created)


class ProfileModelTests(TestCase):

    def setUp(self) -> None:
        User.objects.create_user(
            email='user1@gmail.com',
            first_name='John',
            last_name='Doe',
            password='password',
        )

    def test_model_verbose_name_single(self):
        """Test that model verbose name is set correctly."""
        self.assertEqual(Profile._meta.verbose_name, _('profile'))

    def test_model_verbose_name_plural(self):
        """Test that model verbose name (in plural) is set correctly."""
        self.assertEqual(Profile._meta.verbose_name_plural, _('profiles'))

    def test_profile_image_field_params(self):
        """Test that profile_image field has all required parameters."""
        profile_image_field = Profile._meta.get_field('profile_image')

        self.assertEqual(profile_image_field.verbose_name, _('profile image'))
        self.assertTrue(profile_image_field.blank)
        self.assertTrue(profile_image_field.null)
        self.assertEqual(profile_image_field.upload_to, get_profile_image_upload_path)

    def test_date_of_birth_field_params(self):
        """Test that date_of_birth field has all required parameters."""
        date_of_birth_field = Profile._meta.get_field('date_of_birth')

        self.assertEqual(date_of_birth_field.verbose_name, 'date of birth')
        self.assertTrue(date_of_birth_field.blank)
        self.assertTrue(date_of_birth_field.null)

    def test_gender_field_params(self):
        """Test that gender field has all required parameters."""
        gender_field = Profile._meta.get_field('gender')

        self.assertEqual(gender_field.verbose_name, 'gender')
        self.assertTrue(gender_field.blank)
        self.assertEqual(gender_field.max_length, 2)
        self.assertEqual(gender_field.choices, ProfileGenderChoices.choices)

    def test_description_field_params(self):
        """Test that description field has all required parameters."""
        description_field = Profile._meta.get_field('description')

        self.assertEqual(description_field.verbose_name, _('description'))
        self.assertTrue(description_field.blank)

    def test_object_name_has_user_object_name(self):
        """Test that Profile object name is set up properly."""
        test_profile: Profile = Profile.objects.get(user=User.objects.first())
        self.assertEqual(str(test_profile), f'Profile for {test_profile.user}')


class SettingsModelTests(TestCase):

    def setUp(self) -> None:
        User.objects.create_user(
            email='user1@gmail.com',
            first_name='John',
            last_name='Doe',
            password='password',
        )

    def test_model_verbose_name_single(self):
        """Test that model verbose name is set correctly."""
        self.assertEqual(Settings._meta.verbose_name, _('settings'))

    def test_model_verbose_name_plural(self):
        """Test that model verbose name (in plural) is set correctly."""
        self.assertEqual(Settings._meta.verbose_name_plural, _('settings'))

    def test_currency_field_params(self):
        """Test that currency field has all required parameters."""
        currency_field = Settings._meta.get_field('currency')

        self.assertEqual(currency_field.verbose_name, 'currency')
        self.assertTrue(currency_field.blank)
        self.assertEqual(currency_field.max_length, 2)
        self.assertEqual(currency_field.choices, SettingsСurrencyChoices.choices)

    def test_telegram_id_field_params(self):
        """Test that telegram_id field has all required parameters."""
        telegram_id_field = Settings._meta.get_field('telegram_id')

        self.assertEqual(telegram_id_field.verbose_name, _('user telegram id'))
        self.assertTrue(telegram_id_field.blank)

    def test_object_name_has_user_object_name(self):
        """Test that Settings object name is set up properly."""
        test_settings: Settings = Settings.objects.get(user=User.objects.first())
        self.assertEqual(str(test_settings), f'Settings for {test_settings.user}')
