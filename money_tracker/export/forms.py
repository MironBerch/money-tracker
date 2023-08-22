from django import forms


class ExportTransactionsForm(forms.Form):
    """Form for export user transactions."""

    FORMAT_CHOICES = [
        ('xlsx', 'XLSX'),
        ('csv', 'CSV'),
        ('pdf', 'PDF'),
    ]
    format = forms.ChoiceField(choices=FORMAT_CHOICES, widget=forms.Select)
