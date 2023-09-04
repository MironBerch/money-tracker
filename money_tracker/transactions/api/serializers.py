from rest_framework import serializers

from categories.api.serializers import CategorySerializer
from transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    """Transaction model serializer."""

    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = (
            'id',
            'user',
            'amount',
            'category',
            'cost_accounting_date',
            'transaction_date',
        )
