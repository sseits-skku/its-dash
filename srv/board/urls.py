from django.urls import path
from .views import PostView, CommentView, CategoryView, TagView


urlpatterns = [
    path('comment', CommentView.as_view()),
    path('comment/<int:comment_id>', CommentView.as_view()),
    path('tag', TagView.as_view()),
    path('tag/<str:tag_name>', TagView.as_view()),
    path('category', CategoryView.as_view()),
    path('category/<str:category_name>', CategoryView.as_view()),
    path('board/<str:category_name>', PostView.as_view()),
    path('board/<str:category_name>/<int:post_id>', PostView.as_view()),
]
