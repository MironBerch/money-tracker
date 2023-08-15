from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import redirect
from django.utils.text import slugify
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from categories.forms import CategoryForm
from categories.services import get_user_categories


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
            category.slug = slugify(category.name)
            category.user = request.user
            category.save()
            return redirect('expenses_list')
