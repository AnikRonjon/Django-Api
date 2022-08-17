from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostsView.as_view(), name='posts'),
    path('<int:pk>/', views.PostView.as_view(), name='posts'),
]