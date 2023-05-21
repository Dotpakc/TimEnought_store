from django.contrib import admin

# Register your models here.
from .models import Article, BlogCategory

admin.site.register(Article)
admin.site.register(BlogCategory)