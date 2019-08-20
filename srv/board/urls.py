from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, TagViewSet,    \
                   PostStatusViewSet, PostViewSet, \
                   CommentViewSet

router = routers.DefaultRouter()
router.register('tag', TagViewSet)
router.register('post', PostViewSet)
router.register('comment', CommentViewSet)
router.register('category', CategoryViewSet)
router.register('post-status', PostStatusViewSet)

urlpatterns = [
    path('', include(router.urls))
]
