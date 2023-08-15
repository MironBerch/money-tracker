from django import forms

from categories.models import Category


class CategoryForm(forms.ModelForm):
    """Form for creating new category."""

    class Meta:
        model = Category
        fields = ('name', )
