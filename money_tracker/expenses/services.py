from django.db.models import QuerySet

from accounts.models import User
from expenses.models import Expense


def get_user_expenses(user: User) -> QuerySet[Expense]:
    """Get user `Expense`'s."""
    return Expense.objects.filter(user=user)
