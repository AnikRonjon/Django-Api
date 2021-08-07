from django.views.generic import RedirectView
from django.urls import path
from .import views


app_name = 'blog'
urlpatterns = [
    path('', views.HomeView.as_view(), name='root'),
    path('home/', RedirectView.as_view(url='/'), name='home'),
    path('index/', RedirectView.as_view(url='/'), name='index'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail_view, name='post_detail'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),

]