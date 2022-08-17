from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Post
from .serializer import CategorySerializer, PostSerializer


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serialize = PostSerializer(posts, many=True)
        return Response(serialize.data)

    if request.method == 'POST':
        serialize = PostSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(serialize.data)


