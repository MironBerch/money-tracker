from django import forms

from categories.models import Category
from expenses.models import Transaction


class TransactionForm(forms.ModelForm):
    """Form for creating new expense."""

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
            'expense_date',
        )
