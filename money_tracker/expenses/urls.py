from django.urls import path

from expenses.views import (
    CategoryTransactionsView,
    TransactionCreateView,
    TransactionDetailView,
    TransactionsListView,
    TransactionUpdateView,
)

urlpatterns = [
    path(
        route='expenses-list/',
        view=TransactionsListView.as_view(),
        name='expenses_list',
    ),
    path(
        route='expenses-create/',
        view=TransactionCreateView.as_view(),
        name='expense_create',
    ),
    path(
        route='expenses-list/<slug:slug>/',
        view=CategoryTransactionsView.as_view(),
        name='expense_create',
    ),
    path(
        route='expense/<int:id>/',
        view=TransactionDetailView.as_view(),
        name='expense_detail',
    ),
    path(
        route='expense-update/<int:id>/',
        view=TransactionUpdateView.as_view(),
        name='expense_update',
    ),
]
