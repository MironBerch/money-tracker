from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

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


def get_category_by_id(id: int) -> Category:
    """Return category by id."""
    return get_object_or_404(Category, id=id)


def get_category_by_slug(slug: str) -> Category:
    """Return category by slug."""
    return get_object_or_404(Category, slug=slug)
