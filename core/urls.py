from django.contrib import admin
from blog.admin import blog_admin_site
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from .schema import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog-admin/', blog_admin_site.urls),
    path('api/graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    path('api/rest/', include('api.rest.urls')),
    path('', include('blog.urls', namespace='blog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
