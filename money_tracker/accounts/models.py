from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Custom `User` model."""

    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=100,
        unique=True,
    )

    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=40,
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=40,
    )

    date_joined = models.DateTimeField(
        verbose_name=_('date joined'),
        auto_now_add=True,
    )
    last_login = models.DateTimeField(
        verbose_name=_('last login'),
        auto_now=True,
    )

    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
    )
    is_staff = models.BooleanField(
        verbose_name=_('staff'),
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name=_('superuser'),
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


def get_profile_image_upload_path(instance: 'Profile', filename: str) -> str:
    return f'upload/users/{instance.user.email}/profile/{filename}'


class ProfileGenderChoices(models.TextChoices):
    MALE = 'M', 'Мужской'
    FEMALE = 'F', 'Женский'
    OTHER = 'N', 'Не указывать'


class Profile(models.Model):
    """Profile for `User`."""

    profile_image = models.ImageField(
        verbose_name=_('profile image'),
        blank=True,
        null=True,
        upload_to=get_profile_image_upload_path,
    )
    date_of_birth = models.DateField(
        verbose_name=_('date of birth'),
        blank=True,
        null=True,
    )
    gender = models.CharField(
        verbose_name=_('gender'),
        blank=True,
        max_length=2,
        choices=ProfileGenderChoices.choices,
    )
    description = models.TextField(
        verbose_name=_('description'),
        blank=True,
    )
    user: User = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def __str__(self):
        return f'Profile for {self.user}'


class SettingsСurrencyChoices(models.TextChoices):
    RUB = 'R', 'Ruble'
    USD = 'D', 'Dollar'
    EUR = 'E', 'Euro'

    @classmethod
    def get_default(cls):
        return cls.RUB


class Settings(models.Model):
    """Settings for `User`."""

    telegram_id = models.CharField(
        verbose_name=_('user telegram id'),
        blank=True,
        max_length=50,
    )
    currency = models.CharField(
        verbose_name=_('currency'),
        blank=True,
        max_length=2,
        choices=SettingsСurrencyChoices.choices,
        default=SettingsСurrencyChoices.get_default,
    )
    user: User = models.OneToOneField(
        User,
        related_name='settings',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('settings')
        verbose_name_plural = _('settings')

    def __str__(self):
        return f'Settings for {self.user}'


class TelegramUserVerifyCode(models.Model):
    """Code for connecting the `User` with the telegram user."""

    telegram_code = models.CharField(
        verbose_name=_('6 digits code'),
        unique=True,
        blank=True,
        max_length=6,
        validators=[
            MinLengthValidator(6),
        ],
    )
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
    )
    user: User = models.OneToOneField(
        User,
        related_name='telegram_verify_code',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('telegram code')
        verbose_name_plural = _('telegram codes')

    def __str__(self):
        return f'Code for `{self.telegram_code}` for {self.user}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from .tasks import delete_telegram_verify_code

        delete_telegram_verify_code.apply_async((self.id,), countdown=600)
