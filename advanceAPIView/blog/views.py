from rest_framework import generics
from rest_framework.response import Response
from .models import Category, Post
from .serializer import PostSerializer


# # List View (method 1)
# # in urls.py file add
# # path('', views.PostListView.as_view())
# class PostListView(generics.ListAPIView):
#     def get_queryset(self):
#         return Post.objects.all()
#
#     def get_serializer_class(self):
#         return PostSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListCreateApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveDestroyApiView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
