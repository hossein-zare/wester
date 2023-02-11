from rest_framework.permissions import BasePermission

class CanUser(BasePermission):
    """
    Check if the user can do the given action.
    """

    def __init__(self, action):
        self.action = action

    def has_permission(self, request, view):
        return getattr(request.user.permission, self.action)

    def __call__(self):
        return self

class IsGuest(BasePermission):
    """
    Allows access only to guest users (unauthenticated).
    """

    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)