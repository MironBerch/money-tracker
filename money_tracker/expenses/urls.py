from django.urls import path

from expenses.views import CategoryCreateView, ExpensesListView

urlpatterns = [
    # categories urls
    path(
        route='categories/create/',
        view=CategoryCreateView.as_view(),
        name='create_category',
    ),

    # expenses urls
    path(
        route='expenses-list/',
        view=ExpensesListView.as_view(),
        name='expenses_list',
    ),
]
