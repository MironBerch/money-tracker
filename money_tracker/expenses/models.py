from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from categories.models import Category


class Transaction(models.Model):
    """Expenses model."""

    user: User = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name=_('expense author'),
    )

    amount = models.FloatField(
        validators=[MinValueValidator(0.0)],
        verbose_name=_('expense amount'),
    )
    name = models.CharField(
        verbose_name=_('expense name'),
        max_length=50,
    )
    description = models.TextField(
        verbose_name=_('expense description'),
        max_length=500,
        blank=True,
    )

    category: Category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name=_('expense category'),
    )

    cost_accounting_date = models.DateField(
        auto_now_add=True,
        verbose_name=_('cost accounting date'),
    )
    modified_date = models.DateField(
        auto_now=True,
        verbose_name=_('expense modified date'),
    )
    expense_date = models.DateField(
        editable=True,
        verbose_name=_('date of expense'),
    )

    class Meta:
        ordering = ('-expense_date', )
        verbose_name = _('expense')
        verbose_name_plural = _('expenses')

    def __str__(self):
        return f'{self.name}'
