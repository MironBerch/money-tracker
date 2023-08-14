from django.urls import path

from expenses.views import ExpensesListView

urlpatterns = [
    path(
        route='expenses-list/',
        view=ExpensesListView.as_view(),
        name='expenses_list',
    ),
]
