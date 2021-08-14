from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from blog.models import Post, User
from .serializers import PostSerializer, UserSerializer
from .pagination import MyPagination


class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_class = [IsAdminUser, DjangoModelPermissions]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPagination


class UserCreateAPIView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_class = [IsAdminUser, DjangoModelPermissions]
    # authentication_classes = [JWTAuthentication]
