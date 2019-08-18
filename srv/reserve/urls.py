from django.urls import path
from .views import Seminar, Card


urlpatterns = [
    path('card/<int:id>', Card.as_view(), name='notice'),
    path('seminar/<int:id>', Seminar.as_view(), name='service'),
]
