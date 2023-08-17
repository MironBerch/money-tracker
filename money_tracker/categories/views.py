from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from categories.forms import CategoryForm
from categories.services import get_user_categories, get_user_category_by_slug, user_category_exist
from common.utils import create_slug


class CategoryListView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """View list of categories."""

    template_name = 'categories/categories_list.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response(
            context={
                'categories': get_user_categories(
                    user=request.user,
                ),
            },
        )


class CategoryCreateView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """View for creating new category."""

    form_class = CategoryForm
    template_name = 'categories/category_create.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response(
            context={
                'form': self.form_class(),
            },
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            if user_category_exist(
                user=category.user,
                slug=create_slug(category.name),
            ):
                return redirect('create_category')
            category.save()
            return redirect('categories_list')


class CategoryUpdateView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """View for update category."""

    template_name = 'categories/update_category.html'

    def get(self, request, slug):
        form = CategoryForm(
            request.POST or None,
            instance=get_user_category_by_slug(
                user=request.user,
                slug=slug,
            ),
        )

        return self.render_to_response(
            context={
                'form': form,
            },
        )

    def post(self, request, slug):
        form = CategoryForm(
            request.POST or None,
            instance=get_user_category_by_slug(
                user=request.user,
                slug=slug,
            ),
        )

        if form.is_valid():
            category = form.save()
            category.save()
            return redirect(
                'update_category',
                slug=category.slug,
            )

        return redirect('update_category', slug=slug)
