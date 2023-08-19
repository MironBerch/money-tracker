from django import forms

from categories.models import Category
from transactions.models import Transaction


class TransactionForm(forms.ModelForm):
    """Form for creating new transaction."""

    def __init__(self, user, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)

    class Meta:
        model = Transaction
        fields = (
            'amount',
            'name',
            'description',
            'category',
            'transaction_date',
        )
