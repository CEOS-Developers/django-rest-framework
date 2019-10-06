from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PostsView, PostView

urlpatterns = [
    path('posts/', PostsView.as_view(), name='post-list'),
    path('post/<int:pk>', PostView.as_view(), name='post-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)