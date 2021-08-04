import graphene
from graphene_django import DjangoObjectType, DjangoListField
from blog.models import Post
from django.contrib.auth.models import User


# Create your Schema Query and Mutation from here
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username')


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = '__all__'

    @classmethod
    def get_queryset(cls, queryset, info):
        if info.context.user.is_authenticated():
            return Post.objects.all()
        else:
            return Post.objects.none()


class Query(graphene.AbstractType):
    all_post = graphene.List(PostType)
    detail_post = graphene.Field(PostType, id=graphene.ID())

    def resolve_all_post(self, info, **kwargs):
        return Post.objects.all()

    def resolve_detail_post(self, info, id, **kwargs):
        return Post.objects.get(id=id)


# Create Post Mutations
class PostInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String(required=True)
    author = graphene.String(required=True)
    body = graphene.String(required=True)
    status = graphene.String(required=True)


# class CreatePost(graphene.AbstractType):
#     post_view = graphene.Field(PostType)
#
#     class Arguments:
#         post_data = PostInput(required=True)
#
#     def mutate(self):
#         post =
# class Mutation(graphene.AbstractType):
#     create_post = CreatePost.Field()
