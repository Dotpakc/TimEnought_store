from django.contrib import admin
from .models import Category,Product, Image


class ProductCategoryInline(admin.TabularInline):
    model = Product.category.through
    extra = 1
    
class ImageInline(admin.TabularInline):
    model = Image
    fields = ('product', 'image_tag', 'image', 'is_main')
    readonly_fields = ('image_tag',)
    extra = 1


admin.site.register(Image)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # list_display = ('name', 'image_tag_thumbnail')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('image_tag_thumbnail',)
    fields = ('name', 'slug', 'parent', 'description','image_tag_thumbnail', 'image',
                'meta_title', 'meta_description', 'meta_keywords')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'quantity', 'price', 'is_checked', 'user',
              'meta_title', 'meta_description', 'meta_keywords')
    list_display = ('id', 'name', 'user', 'quantity', 'price', 'is_checked')
    list_display_links = ('id', 'name')
    inlines = (ProductCategoryInline, ImageInline)


