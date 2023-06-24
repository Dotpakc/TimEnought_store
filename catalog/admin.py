from django.contrib import admin
from .models import Category,Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # list_display = ('name', 'image_tag_thumbnail')
    prepopulated_fields = {'slug': ('name',)}
    
    readonly_fields = ('image_tag_thumbnail',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass