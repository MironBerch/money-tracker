from django.contrib import admin

from expenses.models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'amount',
        'name',
        'category',
        'cost_accounting_date',
        'expense_date',
    )
    search_fields = (
        'user',
        'category',
        'expense_date',
    )
    readonly_fields = (
        'id',
        'modified_date',
        'cost_accounting_date',
    )
    list_filter = (
        'user',
        'category',
    )
    ordering = ('user', )
