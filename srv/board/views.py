from rest_framework.viewsets import ModelViewSet as mvs
from .models import Category, Tag, Comment, PostStatus, Post
from .serializers import CategorySerializer, TagSerializer, \
                         CommentSerializer, PostSerializer, \
                         PostStatusSerializer


class CategoryViewSet(mvs):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(mvs):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentViewSet(mvs):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostViewSet(mvs):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostStatusViewSet(mvs):
    queryset = PostStatus.objects.all()
    serializer_class = PostStatusSerializer
