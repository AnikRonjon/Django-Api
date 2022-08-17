from django.contrib import admin
from .models import Category, Post


# Register your models here.
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('title', 'category', 'created', 'updated')
