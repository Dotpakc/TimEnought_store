from django.contrib import admin

from .models import Page
# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'index')
    list_filter = ('is_active', )
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('name', 'slug')
    list_editable = ('is_active', 'index')
    
    fields = ('name', 'slug', 'content', 'is_active', 'meta_title', 'meta_description', 'meta_keywords')