from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from categories.forms import CategoryForm


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
