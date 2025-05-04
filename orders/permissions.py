from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.customer == request.user

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
