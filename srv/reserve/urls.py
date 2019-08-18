from django.urls import path
from .views import Seminar, Card


urlpatterns = [
    path('card/', Card.as_view()),
    path('card/<int:card_id>', Card.as_view()),
    path('seminar/<int:seminar_id>', Seminar.as_view()),
    path('seminar/<str:room_name>/<int:seminar_id>', Seminar.as_view()),
]
