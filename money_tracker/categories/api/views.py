from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from categories.api.serializers import CategorySerializer
from categories.services import get_user_categories, user_category_exist
from common.utils import create_slug


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


class CategoryCreateAPIView(APIView):
    """API view for create category."""

    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        serializer = CategorySerializer(
            data=request.data,
        )
        if serializer.is_valid():
            if not user_category_exist(
                user=request.user,
                slug=create_slug(
                    serializer.validated_data['name'],
                ),
            ):
                serializer.save(
                    user=request.user,
                    slug=create_slug(
                        serializer.validated_data['name'],
                    ),
                )
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED,
                )

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
