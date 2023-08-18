from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from accounts.models import User
from categories.models import Category
from expenses.models import Expense


def get_user_expenses(user: User) -> QuerySet[Expense]:
    """Get user `Expense`'s."""
    return Expense.objects.filter(user=user)


def get_expenses_by_category(category: Category) -> QuerySet[Expense]:
    """Get `Expense`'s by category."""
    return Expense.objects.filter(category=category)


def get_expense_by_id(id: int) -> Expense:
    """Get `Expense` by id."""
    return get_object_or_404(Expense, id=id)


def get_user_expense_by_id(user: User, id: int) -> Expense:
    """Get `Expense` by id."""
    return get_object_or_404(Expense, user=user, id=id)
