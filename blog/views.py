from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post_detail.html', {'post': post})


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

