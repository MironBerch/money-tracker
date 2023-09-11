from django.urls import path

from transactions.api.views import (
    ExpenseListAPIView,
    IncomeListAPIView,
    TransactionCreateAPIView,
    TransactionListAPIView,
)
from transactions.views import (
    TransactionCreateView,
    TransactionDetailView,
    TransactionsListView,
    TransactionUpdateView,
)

urlpatterns = [
    path(
        route='transactions-list/',
        view=TransactionsListView.as_view(),
        name='transactions_list',
    ),
    path(
        route='transactions-create/',
        view=TransactionCreateView.as_view(),
        name='transaction_create',
    ),
    path(
        route='transactions-detail/<int:id>/',
        view=TransactionDetailView.as_view(),
        name='transaction_detail',
    ),
    path(
        route='transactions-update/<int:id>/',
        view=TransactionUpdateView.as_view(),
        name='transaction_update',
    ),

    # transactions api urls
    path(
        route='api/transactions-list/',
        view=TransactionListAPIView.as_view(),
    ),
    path(
        route='api/expenses-list/',
        view=ExpenseListAPIView.as_view(),
    ),
    path(
        route='api/incomes-list/',
        view=IncomeListAPIView.as_view(),
    ),
    path(
        route='api/transactions-create/',
        view=TransactionCreateAPIView.as_view(),
    ),
]
