from django.urls import path
from .views import Post, Comment, Category, Tag


urlpatterns = [
    path('comment', Comment.as_view()),
    path('comment/<int:comment_id>', Comment.as_view()),
    path('tag', Tag.as_view()),
    path('tag/<str:tag_name>', Tag.as_view()),
    path('category', Category.as_view()),
    path('category/<str:category_name>', Category.as_view()),
    path('board/<str:category_name>', Post.as_view()),
    path('board/<str:category_name>/<int:post_id>', Post.as_view()),
]
