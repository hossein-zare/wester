from rest_framework import permissions

class CanUser(permissions.BasePermission):
    """
    Check if the user can do the given action.
    """

    def __init__(self, action):
        self.action = action

    def has_permission(self, request, view):
        return getattr(request.user.permission, self.action)

    def __call__(self):
        return self