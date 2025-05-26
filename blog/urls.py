from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogEntryCreateView, BlogListView, BlogDeleteView, BlogDetailView, BlogUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogEntryCreateView.as_view(), name='blog_create'),
    path('list/', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]