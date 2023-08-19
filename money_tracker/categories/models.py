from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from common.utils import create_slug


class Category(models.Model):
    """Category for `Transaction` model."""

    user: User = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name=_('category author'),
    )
    name = models.CharField(
        verbose_name=_('name of category'),
        max_length=50,
    )
    slug = models.SlugField(
        verbose_name=_('slug for category'),
        max_length=50,
    )

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = create_slug(self.name)
        super(Category, self).save(*args, **kwargs)
