from rest_framework.permissions import BasePermission


class IsNotAuthenticated(BasePermission):
    """Check if user not authenticated."""

    def has_permission(self, request, view):
        return request.user.is_authenticated is False

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated is False
