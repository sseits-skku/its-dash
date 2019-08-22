from rest_framework.permissions import (
    AllowAny, IsAuthenticated
)
from rest_framework.viewsets import ModelViewSet as mvs

from .models import Seminar, Room, Card
from .serializers import (
    SeminarSerializer, RoomSerializer, CardSerializer
)
from utils.permissions import (
    IsOwner, IsStaffUser
)


class SeminarViewSet(mvs):
    queryset = Seminar.objects.all()
    serializer_class = SeminarSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            perm_classes = [AllowAny]
        elif self.action in ['create']:
            perm_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            perm_classes = [IsOwner]
        else:
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]


class RoomViewSet(mvs):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            perm_classes = [AllowAny]
        else:
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]


class CardViewSet(mvs):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            perm_classes = [AllowAny]
        elif self.action in ['create']:
            perm_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            perm_classes = [IsOwner]
        else:
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]
