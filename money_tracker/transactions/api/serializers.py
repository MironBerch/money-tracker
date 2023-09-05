from rest_framework import serializers

from accounts.models import User
from categories.api.serializers import CategorySerializer
from categories.models import Category
from transactions.models import Transaction


class TransactionCreateSerializer(serializers.ModelSerializer):
    """Transaction model serializer."""

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
    )

    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Transaction
        fields = (
            'id',
            'user',
            'name',
            'amount',
            'category',
            'transaction_date',
        )


class TransactionSerializer(serializers.ModelSerializer):
    """Transaction model serializer."""

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
    )

    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = (
            'id',
            'user',
            'name',
            'amount',
            'category',
            'cost_accounting_date',
            'transaction_date',
        )
