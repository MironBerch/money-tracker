from django.urls import path

from expenses.views import ExpenseCreateView, ExpensesListView

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
]
