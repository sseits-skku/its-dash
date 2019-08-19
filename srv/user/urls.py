from django.urls import path
from .views import TokenView, PersonView, MemberView


urlpatterns = [
    path('refresh', TokenView.as_view()),
    path('person', PersonView.as_view()),
    path('person/<int:person_id>', PersonView.as_view()),
    path('member', MemberView.as_view()),
    path('member/<int:member_id>', MemberView.as_view()),
]
