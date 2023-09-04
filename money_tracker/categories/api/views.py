from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from categories.api.serializers import CategorySerializer
from categories.services import get_user_categories


class CategoryListAPIView(ListAPIView):
    """API view displayed list of user categories."""

    permission_classes = (IsAuthenticated, )
    serializer_class = CategorySerializer

    def get_queryset(self):
        return (
            get_user_categories(
                user=self.request.user,
            ).order_by('-id')
        )
