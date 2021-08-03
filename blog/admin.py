from django.contrib import admin
from .models import Post


# Custom Admin Page
class BlogAdmin(admin.AdminSite):
    site_title = 'Learners Choice'
    site_header = 'Login Panel'
    index_title = 'Welcome to contribute with us'


blog_admin_site = BlogAdmin(name='blog-admin')


# # Main Admin Page
# @admin.register(Post)
@admin.register(Post, site=blog_admin_site)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status')
    list_display_links = ('title', 'author', 'publish')
    list_editable = ('status',)
    list_filter = ('author', 'status')
    radio_fields = {'status': admin.HORIZONTAL}
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
