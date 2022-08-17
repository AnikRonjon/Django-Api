from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Category, Post
from .serializer import PostSerializer


# Method 1
class PostListView(GenericAPIView, mixins.ListModelMixin):
    def get_queryset(self):
        return Post.objects.all()

    def get_serializer_class(self):
        return PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# Method 2 (shorthand)
class PostRetriveView(GenericAPIView, mixins.RetrieveModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostUpdateView(GenericAPIView, mixins.UpdateModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)