import django_filters

from django import forms

from categories.models import Category
from transactions.models import Transaction


class TransactionForm(forms.ModelForm):
    """Form for creating new transaction."""

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingInput',
            },
        ),
    )
    amount = forms.FloatField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingInput',
                'type': 'number',
                'step': '0.1',
            },
        ),
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'floatingInput',
                'rows': '3',
            },
        ),
    )
    category = forms.ModelChoiceField(
        queryset=None,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'aria-label': 'Select category for transaction',
                'id': 'floatingInput',
            },
        ),
    )
    transaction_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select a date',
            },
        ),
    )

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


class TransactionFilter(django_filters.FilterSet):
    """Form for filter transaction queryset."""

    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Search by name',
            },
        ),
    )

    amount__gt = django_filters.NumberFilter(
        field_name='amount',
        lookup_expr='gt',
        label='Amount greater than',
        widget=forms.NumberInput(
            attrs={
                'type': 'number',
                'step': '0.1',
                'class': 'form-control',
                'placeholder': 'Enter amount greater than',
            },
        ),
    )
    amount__lt = django_filters.NumberFilter(
        field_name='amount',
        lookup_expr='lt',
        label='Amount less than',
        widget=forms.NumberInput(
            attrs={
                'type': 'number',
                'step': '0.1',
                'class': 'form-control',
                'placeholder': 'Enter amount less than',
            },
        ),
    )
    category = django_filters.ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.none(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'aria-label': 'Select category for transaction',
                'id': 'floatingInput',
            },
        ),
    )

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['category'].queryset = Category.objects.filter(user=user)

    class Meta:
        model = Transaction
        fields = (
            'category',
            'amount__gt',
            'amount__lt',
            'name',
        )
