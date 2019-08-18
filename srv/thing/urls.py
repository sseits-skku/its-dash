from django.urls import path
from .views import ThingType, Thing, Seat


urlpatterns = [
    path('_thingtype/<int:id>', ThingType.as_view(), name='notice'),
    path('thing/<int:id>', Thing.as_view(), name='service'),
    path('seat/<int:id>', Seat.as_view(), name='recruit'),
]
