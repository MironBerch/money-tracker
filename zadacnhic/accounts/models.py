from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Custom `User` model."""

    email = models.EmailField(
        _('email address'),
        max_length=100,
        unique=True,
    )

    first_name = models.CharField(
        _('first name'),
        max_length=40,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=40,
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
    )
    is_staff = models.BooleanField(
        _('staff'),
        default=False,
    )
    is_superuser = models.BooleanField(
        _('superuser'),
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
        return f"{self.first_name} {self.last_name}"
