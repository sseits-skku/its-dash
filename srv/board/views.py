from rest_framework.viewsets import ModelViewSet as mvs
from rest_framework.permissions import (
    AllowAny, IsAuthenticated
)

from .models import Category, Tag, Comment, PostStatus, Post
from .serializers import (
    CategorySerializer, TagSerializer, CommentSerializer,
    PostSerializer, PostStatusSerializer
)
from utils.permissions import (
    IsOwner, IsStaffUser
)


class CategoryViewSet(mvs):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            perm_classes = [AllowAny]
        else:
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]


class TagViewSet(mvs):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            perm_classes = [AllowAny]
        else:
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]


class CommentViewSet(mvs):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['retrieve']:
            perm_classes = [AllowAny]
        elif self.action in ['create']:
            perm_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            perm_classes = [IsOwner]
        else:  # destroy, list
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]


class PostViewSet(mvs):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ['retrieve']:
            perm_classes = [AllowAny]
        elif self.action in ['create']:
            perm_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            perm_classes = [IsOwner]
        else:  # destroy, list
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]


class PostStatusViewSet(mvs):
    queryset = PostStatus.objects.all()
    serializer_class = PostStatusSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            perm_classes = [AllowAny]
        else:
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]
