from rest_framework.viewsets import ModelViewSet as mvs
from .models import IPAddress
from .serializers import IPAddressSerializer


class IPAddressViewSet(mvs):
    queryset = IPAddress.objects.all()
    serializer_class = IPAddressSerializer
