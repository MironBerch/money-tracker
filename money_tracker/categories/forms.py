from django import forms

from categories.models import Category


class CategoryForm(forms.ModelForm):
    """Form for creating new category."""

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': 'Category name',
            },
        ),
    )

    class Meta:
        model = Category
        fields = ('name', )
