from rest_framework.viewsets import ModelViewSet as mvs
from rest_framework_jwt.authentication import JSONWebTokenAuthentication as JWTAuth    # noqa: E501

from .models import IPAddress
from .serializers import IPAddressSerializer
from utils.permissions import IsAdminUser


class IPAddressViewSet(mvs):
    queryset = IPAddress.objects.all()
    serializer_class = IPAddressSerializer
    permission_classes = [IsAdminUser]
