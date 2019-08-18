from django.urls import path
from .views import Token, Person, Member


urlpatterns = [
    path('token/<int:id>', Token.as_view(), name='notice'),
    path('person/<int:id>', Person.as_view(), name='service'),
    path('member/<int:id>', Member.as_view(), name='recruit'),
]
