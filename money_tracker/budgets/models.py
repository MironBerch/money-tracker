from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class Budget(models.Model):
    """Budget for `User`."""

    budget = models.FloatField(
        verbose_name=_('overall budget'),
        default=0,
    )

    user: User = models.OneToOneField(
        User,
        related_name=_('budget'),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('budget')
        verbose_name_plural = _('budgets')

    def __str__(self):
        return f'{self.budget}'
