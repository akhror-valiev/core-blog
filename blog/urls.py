from django.urls import path
from django.urls import reverse
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDetailView,
    PostDeleteView,
    UserPostListView,
    PostCommentView,
    LikeView
)
from . import views



urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/comment/', PostCommentView.as_view(), name = 'add-comment'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('about/', views.about, name = 'blog-about'),
    path('contact/', views.contact, name = 'blog_contact'),
    path('like/<int:pk>/', LikeView, name = 'like_post'),
]