from django.urls import path
from rest_framework.generics import ListCreateAPIView
from rest_framework.urlpatterns import format_suffix_patterns

from api import views
from api.models import Post, Comment
from api.serializers import PostSerializer

urlpatterns = [
    path('posts/', ListCreateAPIView.as_view(queryset=Post.objects.all(), serializer_class=PostSerializer), name='post-list')
]

urlpatterns = format_suffix_patterns(urlpatterns)  # 이 코드 추가하면 다른 추가적인 url 패턴은 필요하지 않음
