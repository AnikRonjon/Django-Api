from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Post
from .serializer import CategorySerializer, PostSerializer


# Create your views here.
@api_view(['GET'])
def posts_view(request):
    posts = Post.objects.all()
    serialize = PostSerializer(posts, many=True)
    return Response(serialize.data)
