from rest_framework import status
from django.http import Http404
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Post, Comment
from api.serializers import PostSerializer
#from rest_framework import generics

# CBV 뷰 방식
class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


''' FBV 방식
@api_view(['GET', 'POST'])  # 함수 기반 뷰 작업을 위한 wrapper
def post_list(request, format=None):  # format 인자 추가 - 다양한 형식의 response를 유연하게 지원

    if request.method =='GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # postman에서 params가 아닌 body에 {"text": "새로운 post"} 요청 보내야 함
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # status 모듈 통해 좀더 명확한 식별자 사용
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

''' 간단한 generic CBV 방식
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''
