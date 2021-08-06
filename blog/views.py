from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Post


# Create your views here.
class HomeView(TemplateView):
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(status='published')
        return context