from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class Category(models.Model):
    """Category for `Expense` model."""

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name=_('category author'),
    )
    name = models.CharField(
        verbose_name=_('name of category'),
        max_length=50,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name=_('slug for category'),
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return f'{self.name}'
