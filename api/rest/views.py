from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from blog.models import Post
from .serializers import PostSerializer


class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_class = [IsAdminUser, DjangoModelPermissions]
    # authentication_classes = [JWTAuthentication]


class UserCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_class = [IsAdminUser, DjangoModelPermissions]
    # authentication_classes = [JWTAuthentication]
