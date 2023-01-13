from rest_framework import permissions
from rest_framework.permissions import IsAdminUser

class OrderPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True

        return bool(request.user and request.user.is_authenticated and request.user.is_staff)

class OrderToPuPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method == 'PUT':
            return request.user.is_staff
        return False

class ProfilePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)