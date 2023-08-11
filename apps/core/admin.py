from django.contrib import admin

from .models import Page, ProductSet
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

class ProductInline(admin.TabularInline):
    model = ProductSet.products.through
    extra = 1
    verbose_name = 'Товар'
    verbose_name_plural = 'Товари'


@admin.register(ProductSet)
class ProductSetAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort', 'is_active')
    list_filter = ('is_active', 'sort')
    search_fields = ('name', )
    list_display_links = ('name', )
    list_editable = ('is_active', 'sort')
    
    fields = ('name', 'products', 'is_active', 'sort')
    inlines = [ProductInline, ]
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('products')