from django.urls import path
from .views import ThingTypeView, ThingView, SeatView


urlpatterns = [
    path('_thingtype/<int:ttype_id>', ThingTypeView.as_view()),
    path('thing/<int:thing_id>', ThingView.as_view()),
    path('seat/<int:seat_id>', SeatView.as_view()),
]
