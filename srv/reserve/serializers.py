from rest_framework.serializers import ModelSerializer as ms

from .models import Room, Seminar, Card


class CardSerializer(ms):
    class Meta:
        model = Card
        fields = '__all__'


class RoomSerializer(ms):
    class Meta:
        model = Room
        fields = '__all__'


class SeminarSerializer(ms):
    class Meta:
        model = Seminar
        fields = '__all__'
