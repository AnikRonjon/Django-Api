from django.views.generic import TemplateView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
class HomeView(TemplateView):
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(status='published')
        return context


def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post_detail.html', {'post': post})