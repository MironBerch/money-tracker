from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from categories.models import Category
from transactions.managers import TransactionManager


class Transaction(models.Model):
    """Transactions model."""

    user: User = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name=_('transaction author'),
    )

    amount = models.FloatField(
        validators=[MinValueValidator(0.0)],
        verbose_name=_('transaction amount'),
    )
    name = models.CharField(
        verbose_name=_('transaction name'),
        max_length=50,
    )
    description = models.TextField(
        verbose_name=_('transaction description'),
        max_length=500,
        blank=True,
    )

    category: Category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name=_('transaction category'),
    )

    cost_accounting_date = models.DateField(
        auto_now_add=True,
        verbose_name=_('cost accounting date'),
    )
    modified_date = models.DateField(
        auto_now=True,
        verbose_name=_('transaction modified date'),
    )
    transaction_date = models.DateField(
        editable=True,
        verbose_name=_('date of transaction'),
    )

    objects = TransactionManager()

    class Meta:
        ordering = ('-transaction_date', )
        verbose_name = _('transaction')
        verbose_name_plural = _('transactions')

    def __str__(self):
        return f'{self.name}'
