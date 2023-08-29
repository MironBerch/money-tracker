from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from transactions.forms import TransactionFilter, TransactionForm
from transactions.services import get_user_transaction_by_id, get_user_transactions


class TransactionsListView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """View list of transactions."""

    template_name = 'transactions/transactions_list.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        transactions = TransactionFilter(
            user=request.user,
            data=request.GET,
            queryset=get_user_transactions(
                user=request.user,
            ),
        )
        return self.render_to_response(
            context={
                'transactions': transactions,
            },
        )


class TransactionCreateView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """View for creating new transaction."""

    form_class = TransactionForm
    template_name = 'transactions/transactions_create.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response(
            context={
                'form': self.form_class(
                    user=request.user,
                ),
            },
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        form = TransactionForm(
            user=request.user,
            data=request.POST or None,
        )
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transactions_list')


class TransactionDetailView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """Detail transaction view."""

    template_name = 'transactions/transactions_detail.html'

    def get(self, request, id):
        return self.render_to_response(
            context={
                'transaction': get_user_transaction_by_id(
                    user=request.user,
                    id=id,
                ),
            },
        )


class TransactionUpdateView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """View for updating transaction."""

    template_name = 'transactions/transactions_update.html'

    def get(self, request, id):
        form = TransactionForm(
            user=request.user,
            instance=get_user_transaction_by_id(
                user=request.user,
                id=id,
            ),
        )

        return self.render_to_response(
            context={
                'form': form,
            },
        )

    def post(self, request: HttpRequest, id, *args, **kwargs):
        form = TransactionForm(
            user=request.user,
            data=request.POST or None,
            instance=get_user_transaction_by_id(
                user=request.user,
                id=id,
            ),
        )

        if form.is_valid():
            form.save()
            return redirect('transactions_list')

        return redirect('transactions_list')
