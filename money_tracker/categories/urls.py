from django.urls import path

from categories.views import CategoryCreateView, CategoryListView, CategoryUpdateView

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
    path(
        route='categories/<slug:slug>/update/',
        view=CategoryUpdateView.as_view(),
        name='update_category',
    ),
]
