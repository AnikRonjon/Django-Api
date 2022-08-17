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



