from django.urls import reverse

from config.settings import PAGE_NAMES

from .models import Category, Product


from apps.main.mixins import ListViewBreadcrumbMixin, DetailViewBreadcrumbMixin

class CatalogIndexView(ListViewBreadcrumbMixin):
    template_name = 'catalog/index.html'
    model = Category
    
    def get_queryset(self):
        return Category.objects.filter(parent=None)
    
    def get_breadcrumbs(self):
        self.breadcrumbs = {
           'current' : PAGE_NAMES['catalog'],
        } # вказуємо поточну сторінку ДОПИСАТИ
        return self.breadcrumbs
    
class ProductByCategoryView(ListViewBreadcrumbMixin):
    template_name = 'catalog/category.html'
    category = None
    categories = Category.objects.all()
    paginate_by = 6
    
    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(category=self.category)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = self.categories
        return context
    

class ProductDetailView(DetailViewBreadcrumbMixin):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'
    
    

