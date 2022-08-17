from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Post
from .serializer import PostSerializer


# Create your views here.
class PostsView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serialize = PostSerializer(posts, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = PostSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(serialize.data)


class PostView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serialize = PostSerializer(post)
        return Response(serialize.data)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serialize = PostSerializer(post, data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(serialize.data)





