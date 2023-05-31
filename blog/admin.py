from django.contrib import admin

from .models import Article, Category, Tag
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content', 'category__name']
    list_display = ['title', 'category', 'created_at', 'updated_at']
    list_filter = ['category', 'tags', 'created_at', 'updated_at']

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'slug']
    list_filter = ['name']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)