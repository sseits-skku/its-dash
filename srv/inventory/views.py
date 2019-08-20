from rest_framework.viewsets import ModelViewSet as mvs
from .models import Computer, OSType, Stock,       \
                    StockStatus, StockType
from .serializers import StockStatusSerializer,    \
                         StockTypeSerializer,      \
                         StockSerializer,          \
                         OSTypeSerializer,         \
                         ComputerSerializer


class StockStatusViewSet(mvs):
    queryset = StockStatus.objects.all()
    serializer_class = StockStatusSerializer


class StockTypeViewSet(mvs):
    queryset = StockType.objects.all()
    serializer_class = StockTypeSerializer


class StockViewSet(mvs):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class OSTypeViewSet(mvs):
    queryset = OSType.objects.all()
    serializer_class = OSTypeSerializer


class ComputerViewSet(mvs):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
