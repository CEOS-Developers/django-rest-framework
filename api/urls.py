from django.urls import path
from rest_framework.generics import ListCreateAPIView

from api import views
from api.models import Post, Comment
from api.serializers import PostSerializer

urlpatterns = [
    path('posts/', ListCreateAPIView.as_view(queryset=Post.objects.all(), serializer_class=PostSerializer), name='post-list')
]
