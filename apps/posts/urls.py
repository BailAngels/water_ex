from django.urls import path

from apps.posts.views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='homepage'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]