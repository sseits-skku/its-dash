from django.urls import path
from .views import ThingType, Thing, Seat


urlpatterns = [
    path('_thingtype/<int:ttype_id>', ThingType.as_view()),
    path('thing/<int:thing_id>', Thing.as_view()),
    path('seat/<int:seat_id>', Seat.as_view()),
    path('seat/<int:row>/<int:column>', Seat.as_view()),
]
