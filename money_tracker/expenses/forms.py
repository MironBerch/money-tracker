from django import forms

from expenses.models import Category, Expense


class CategoryForm(forms.ModelForm):
    """Form for creating new category."""

    class Meta:
        model = Category
        fields = ('name', )


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
