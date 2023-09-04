from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from transactions.api.serializers import TransactionSerializer
from transactions.services import get_user_transactions


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
