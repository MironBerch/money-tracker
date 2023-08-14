from django.contrib import admin

from expenses.models import Category, Expense


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'slug',
    )
    search_fields = (
        'user',
        'name',
    )
    prepopulated_fields = {'slug': ('name', )}
    readonly_fields = ('id', )
    ordering = ('user',)
    list_filter = ('user', )


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
