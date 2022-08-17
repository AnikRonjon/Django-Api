from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view()),
    path('<int:pk>/', views.PostRetriveView.as_view()),
    path('update/<int:pk>/', views.PostUpdateView.as_view()),

]