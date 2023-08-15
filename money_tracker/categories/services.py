from django.db.models import QuerySet

from accounts.models import User
from categories.models import Category


def get_user_categories(user: User) -> QuerySet[Category]:
    return (
        Category.objects.filter(
            user=user,
        )
    )
