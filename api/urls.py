from django.urls import path
from rest_framework.generics import ListCreateAPIView

from api import views
from api.models import Post, Comment
from api.serializers import PostSerializer

from .views import PostList

urlpatterns = [
    #path('posts/', ListCreateAPIView.as_view(queryset=Post.objects.all(), serializer_class=PostSerializer), name='post-list'),
    path('posts/', PostList.as_view()),
]
