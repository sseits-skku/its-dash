from django.urls import path
from .views import Notice, Service, Recruit


urlpatterns = [
    path('notice/<int:id>', Notice.as_view(), name='notice'),
    path('service/<int:id>', Service.as_view(), name='service'),
    path('recruit/<int:id>', Recruit.as_view(), name='recruit'),
]
