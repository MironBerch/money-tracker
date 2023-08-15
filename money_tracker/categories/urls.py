from django.urls import path

from categories.views import CategoryCreateView, CategoryListView

urlpatterns = [
    path(
        route='categories/create/',
        view=CategoryCreateView.as_view(),
        name='create_category',
    ),
    path(
        route='categories/list/',
        view=CategoryListView.as_view(),
        name='categories_list',
    ),
]
