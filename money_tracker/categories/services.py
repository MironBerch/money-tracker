from django.db.models import QuerySet

from accounts.models import User
from categories.models import Category


def get_user_categories(user: User) -> QuerySet[Category]:
    """Return categories which created by user."""
    return (
        Category.objects.filter(
            user=user,
        )
    )


def user_category_exist(user: User, slug: str) -> bool:
    """Check that user has category exist."""
    return (
        Category.objects.filter(
            user=user,
            slug=slug,
        ).exists()
    )
