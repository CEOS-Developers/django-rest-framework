from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.serializers import PostSerializer


class PostsView(ListCreateAPIView):
    serializer_class = PostSerializer
    model_class = serializer_class.Meta.model
    queryset = model_class.objects.all()


class PostView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    model_class = serializer_class.Meta.model
    queryset = model_class.objects.all()

# class PostList(ListCreateAPIView):
#     def get(self, request, format=None):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
