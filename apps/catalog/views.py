from typing import Any, Dict
from django.views.generic import ListView, DetailView
from .models import Category, Product

class CatalogIndexView(ListView):
    template_name = 'catalog/index.html'
    model = Category
    
    def get_queryset(self):
        return Category.objects.filter(parent=None)
    
class ProductByCategoryView(ListView):
    template_name = 'catalog/category.html'
    category = None
    categories = Category.objects.all()
    
    
    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(category=self.category)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = self.categories
        return context
    

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'