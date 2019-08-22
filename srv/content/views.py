from rest_framework.viewsets import ModelViewSet as mvs
from rest_framework.permissions import (
    AllowAny, IsAuthenticated
)

from .models import FileContent, ImageContent
from .serializers import FileContentSerializer, ImageContentSerializer
from utils.permissions import (
    IsOwner, IsStaffUser
)


class ImageContentViewSet(mvs):
    queryset = ImageContent.objects.all()
    serializer_class = ImageContentSerializer

    def get_attribute(self, instance):
        print(f"{instance.member_only}/{self.context['request'].user.is_staff}")
        if not instance.member_only or self.context['request'].user.is_staff:
            return super(FileContentViewSet, self).get_attribute(instance)
        return None

    def get_permissions(self):
        if self.action in ['retrieve']:
            perm_classes = [AllowAny]
        elif self.action in ['create']:
            perm_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            perm_classes = [IsOwner]
        else:  # destroy, list
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]


class FileContentViewSet(mvs):
    queryset = FileContent.objects.all()
    serializer_class = FileContentSerializer

    def get_attribute(self, instance):
        if not instance.member_only or self.context['request'].user.is_staff:
            return super(FileContentViewSet, self).get_attribute(instance)
        return None

    def get_permissions(self):
        if self.action in ['retrieve']:
            perm_classes = [AllowAny]
        elif self.action in ['create']:
            perm_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            perm_classes = [IsOwner]
        else:  # destroy, list
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]
