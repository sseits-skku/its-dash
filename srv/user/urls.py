from django.urls import path
from .views import Token, Person, Member


urlpatterns = [
    path('refresh', Token.as_view()),
    path('person', Person.as_view()),
    path('person/<int:person_id>', Person.as_view()),
    path('member', Member.as_view()),
    path('member/<int:member_id>', Member.as_view()),
]
