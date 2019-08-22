from django.db import models
from rest_framework.permissions import BasePermission


class OwnerMixin(models.Model):
    owner = models.ForeignKey('account.User',
                              on_delete=models.SET_NULL,
                              null=True, blank=True)

    class Meta:
        abstract = True


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and
                    request.user.is_authenticated and
                    request.user == obj.owner)


class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and
                    request.user.is_staff and
                    request.user.is_superuser)


class IsStaffUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
