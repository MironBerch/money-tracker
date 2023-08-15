from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from expenses.forms import CategoryForm
from expenses.services import get_user_expenses


class ExpensesListView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """View list of expenses."""

    template_name = 'expenses/expenses_list.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response(
            context={
                'expenses': get_user_expenses(
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
