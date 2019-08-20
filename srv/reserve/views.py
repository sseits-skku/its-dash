from rest_framework.viewsets import ModelViewSet as mvs
from .models import Seminar, Room, Card
from .serializers import SeminarSerializer, RoomSerializer, \
                         CardSerializer


class SeminarViewSet(mvs):
    queryset = Seminar.objects.all()
    serializer_class = SeminarSerializer


class RoomViewSet(mvs):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CardViewSet(mvs):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
