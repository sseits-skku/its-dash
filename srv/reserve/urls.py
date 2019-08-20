from django.urls import path, include
from rest_framework import routers

from .views import RoomViewSet, CardViewSet, \
                   SeminarViewSet

router = routers.DefaultRouter()
router.register('card', CardViewSet)
router.register('room', RoomViewSet)
router.register('seminar', SeminarViewSet)

urlpatterns = [
    path('', include(router.urls))
]
