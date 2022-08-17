from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from .models import Category, Post
from .serializer import PostSerializer


# Method 1
class PostModelView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Method 2
# class PostModelViews(ModelViewSet):
#     def get_queryset(self):
#         return Post.objects.all()
#
#     def get_serializer_class(self):
#         return PostSerializer


class PostModelViewReadOnly(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

