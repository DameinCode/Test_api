from rest_framework import permissions

class OrderPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        return bool(request.user and request.user.is_authenticated and request.user.is_staff)
