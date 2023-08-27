from django.db.models import Count, QuerySet
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


def get_annotated_user_categories(user: User) -> QuerySet[Category]:
    """Return annotated categories which created by user."""
    return (
        Category.objects.filter(
            user=user,
        ).annotate(
            num_transactions=Count('transaction'),
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


def get_user_category_by_slug(user: User, slug: str) -> Category:
    """Return user's category by slug."""
    return get_object_or_404(Category, user=user, slug=slug)
