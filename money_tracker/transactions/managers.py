from django.db import models


class TransactionManager(models.Manager):
    """Custom manager for `Transaction` model."""

    def get_expenses(self):
        return (
            super().get_queryset().filter(
                amount__lt=0,
            )
        )

    def get_income(self):
        return (
            super().get_queryset().filter(
                amount__gt=0,
            )
        )
