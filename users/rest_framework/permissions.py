from rest_framework.permissions import BasePermission

class IsGuest(BasePermission):
    """
    Allows access only to guest users (unauthenticated).
    """

    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)

class CanUser(BasePermission):
    """
    Check if the user can do the given action.
    """

    def __init__(self, action, methods=None):
        self.action = action
        self.methods = methods

    def has_permission(self, request, view):
        if not self.methods or request.method in self.methods:
            return getattr(request.user.permission, self.action)

        return True

    def __call__(self):
        return self