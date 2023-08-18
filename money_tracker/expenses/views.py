from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from categories.services import get_user_category_by_slug
from expenses.forms import ExpenseForm
from expenses.services import get_expenses_by_category, get_user_expense_by_id, get_user_expenses


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


class ExpenseCreateView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """View for creating new expense."""

    form_class = ExpenseForm
    template_name = 'expenses/expense_create.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response(
            context={
                'form': self.form_class(
                    user=request.user,
                ),
            },
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        form = ExpenseForm(
            request.POST or None,
            user=request.user,
        )
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expenses_list')


class ExpenseDetailView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """Detail expense view."""

    template_name = 'expenses/detail_expense.html'

    def get(self, request, id):
        return self.render_to_response(
            context={
                'expense': get_user_expense_by_id(
                    user=request.user,
                    id=id,
                ),
            },
        )


class ExpenseUpdateView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """View for updating expense."""

    template_name = 'expenses/expense_update.html'

    def get(self, request, id):
        form = ExpenseForm(
            user=request.user,
            instance=get_user_expense_by_id(
                user=request.user,
                id=id,
            ),
        )

        return self.render_to_response(
            context={
                'form': form,
            },
        )


class CategoryExpensesView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """View for category expenses."""

    template_name = 'expenses/category_expenses.html'

    def get(self, request: HttpRequest, slug):
        return self.render_to_response(
            context={
                'expenses': get_expenses_by_category(
                    category=get_user_category_by_slug(
                        user=request.user,
                        slug=slug,
                    ),
                ),
            },
        )
