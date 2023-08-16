from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from expenses.forms import ExpenseForm
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
