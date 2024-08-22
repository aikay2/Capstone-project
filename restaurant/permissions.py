from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Allows access only to safe methods except user is an admin.
    """
    def has_permission(self, request, view):
        return bool(
            request.method in ('GET', 'HEAD', 'OPTIONS') or
            request.user and
            request.user.is_staff
        )