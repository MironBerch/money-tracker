from django import forms

from expenses.models import Expense


class ExpenseForm(forms.ModelForm):
    """Form for creating new expense."""

    class Meta:
        model = Expense
        fields = (
            'amount',
            'name',
            'description',
            'category',
            'expense_date',
        )
