from django.urls import path
from .views import BlogListView, BlogDetailView, CreatePostView, ReservedDetailView

urlpatterns = [
    path('post/', CreatePostView.as_view(), name='add_post'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/', ReservedDetailView.as_view(), name='post_reserved'),
    path('', BlogListView.as_view(), name='home'),
]

