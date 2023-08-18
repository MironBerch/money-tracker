from django.urls import path

from expenses.views import (
    CategoryExpensesView,
    ExpenseCreateView,
    ExpenseDetailView,
    ExpensesListView,
)

urlpatterns = [
    path(
        route='expenses-list/',
        view=ExpensesListView.as_view(),
        name='expenses_list',
    ),
    path(
        route='expenses-create/',
        view=ExpenseCreateView.as_view(),
        name='expense_create',
    ),
    path(
        route='expenses-list/<slug:slug>/',
        view=CategoryExpensesView.as_view(),
        name='expense_create',
    ),
    path(
        route='expense/<int:id>/',
        view=ExpenseDetailView.as_view(),
        name='expense_detail',
    ),
]
