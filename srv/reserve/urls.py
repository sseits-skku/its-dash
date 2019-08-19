from django.urls import path
from .views import SeminarView, CardView


urlpatterns = [
    path('card', CardView.as_view()),
    path('card/<int:card_id>', CardView.as_view()),
    path('seminar', SeminarView.as_view()),
    path('seminar/<int:seminar_id>', SeminarView.as_view()),
    path('seminar/<str:room_name>', SeminarView.as_view()),
]
