from rest_framework import serializers

from accounts.models import User
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Category model serializer."""

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
    )
    slug = serializers.SlugField(
        required=False,
    )

    class Meta:
        model = Category
        fields = (
            'id',
            'user',
            'name',
            'slug',
        )
