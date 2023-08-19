from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from accounts.models import User
from categories.models import Category
from transactions.models import Transaction


def get_user_transactions(user: User) -> QuerySet[Transaction]:
    """Get user `Transaction`'s."""
    return Transaction.objects.filter(user=user)


def get_transactions_by_category(category: Category) -> QuerySet[Transaction]:
    """Get `Transaction`'s by category."""
    return Transaction.objects.filter(category=category)


def get_transaction_by_id(id: int) -> Transaction:
    """Get `Transaction` by id."""
    return get_object_or_404(Transaction, id=id)


def get_user_transaction_by_id(user: User, id: int) -> Transaction:
    """Get `Transaction` by id."""
    return get_object_or_404(Transaction, user=user, id=id)
