from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from accounts.models import User, UserManager


def get_user_by_pk(pk: int | str) -> User | None:
    """Get `User` by primary key."""
    return get_object_or_404(User, pk=pk)


def get_user_by_email(email: str) -> QuerySet[User]:
    """Get `User` by email."""
    return User.objects.filter(email=UserManager.normalize_email(email))
