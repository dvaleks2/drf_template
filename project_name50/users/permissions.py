from rest_framework import permissions

from users.models import User, UserTypes


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have a method get_owner
        return obj.get_owner() == request.user


class IsOwnerOrUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.get_owner() == request.user or obj.get_user() == request.user


class IsPhotographer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.type == UserTypes.PHOTOGRAPHER


class IsUsualUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.type == UserTypes.USUAL


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
