from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from rest_framework.viewsets import ModelViewSet as mvs
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication as JWTAuth

from .serializers import (
    UserSerializer, GroupSerializer, PermissionSerializer
)
from utils.permissions import IsStaffUser, IsOwner

User = get_user_model()


class UserViewSet(mvs):
    queryset = User.objects                  \
                   .order_by('-date_joined') \
                   .all()
    serializer_class = UserSerializer
    authentication_classes = JWTAuth

    def get_permissions(self):
        if self.action in ['create', 'list', 'destroy']:
            perm_classes = [IsStaffUser]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            perm_classes = [IsOwner]
        else:
            perm_classes = []
        return [perm() for perm in perm_classes]


class GroupViewSet(mvs):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = JWTAuth

    def get_permissions(self):
        perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]


class PermissionViewSet(mvs):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    authentication_classes = JWTAuth

    def get_permissions(self):
        perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]
