from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api', views.PostModelView)
router.register('', views.PostModelViewReadOnly)

urlpatterns = router.urls
