from django.views.generic import ListView, DetailView
from .models import Category

class CatalogIndexView(ListView):
    template_name = 'catalog/index.html'
    model = Category
    
    def get_queryset(self):
        return Category.objects.filter(parent=None)