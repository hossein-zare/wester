from rest_framework.permissions import BasePermission

class IsGuest(BasePermission):
    """
    Allows access only to guest users (unauthenticated).
    """

    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)