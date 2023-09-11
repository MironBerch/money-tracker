from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions.api.serializers import TransactionCreateSerializer, TransactionSerializer
from transactions.services import get_user_expenses, get_user_income, get_user_transactions


class TransactionListAPIView(ListAPIView):
    """API view displayed list of user transactions."""

    permission_classes = (IsAuthenticated, )
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return (
            get_user_transactions(
                user=self.request.user,
            ).order_by('-id')
        )


class TransactionCreateAPIView(APIView):
    """API view for create transaction."""

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = TransactionCreateSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ExpenseListAPIView(ListAPIView):
    """API view displayed list of user expenses."""

    permission_classes = (IsAuthenticated, )
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return (
            get_user_expenses(
                user=self.request.user,
            ).order_by('-id')
        )


class IncomeListAPIView(ListAPIView):
    """API view displayed list of user incomes."""

    permission_classes = (IsAuthenticated, )
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return (
            get_user_income(
                user=self.request.user,
            ).order_by('-id')
        )
