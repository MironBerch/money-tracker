from django.db.models import QuerySet

from accounts.models import User
from categories.models import Category
from expenses.models import Expense


def get_user_expenses(user: User) -> QuerySet[Expense]:
    """Get user `Expense`'s."""
    return Expense.objects.filter(user=user)


def get_expenses_by_category(category: Category) -> QuerySet[Expense]:
    """Get `Expense`'s by category."""
    return Expense.objects.filter(category=category)
