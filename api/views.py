from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    #queryset = Post.objects.order_by('-id')
    serializer_class = PostSerializer