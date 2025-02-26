from django.urls import path
from .views import home, about, PostListView, PostDetailView, PostCreateView, delete_post, PostUpdateView

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('delete-item/<int:id>/', delete_post, name='delete-item'),
    path('posts/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
]