from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from rest_framework.viewsets import ModelViewSet as mvs
from .serializers import UserSerializer, GroupSerializer, \
                         PermissionSerializer


User = get_user_model()


class UserViewSet(mvs):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()                          \
                           .order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(mvs):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(mvs):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
