from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    post = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'post')
