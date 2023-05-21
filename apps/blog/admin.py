from django.contrib import admin

# Register your models here.
from .models import Article, BlogCategory, Tag

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(BlogCategory)