from django.shortcuts import get_object_or_404

from accounts.models import User


def get_user_by_pk(pk: int | str) -> User | None:
    """Get `User` by primary key."""
    return get_object_or_404(User, pk=pk)


def get_user_by_email(email: str) -> User | None:
    """Get `User` by email."""
    return get_object_or_404(User, email=email)
