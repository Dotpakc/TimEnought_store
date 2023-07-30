from django.urls import reverse

from config.settings import PAGE_NAMES

from .models import Category, Product

from apps.order.views import get_cart_data
from apps.core.mixins import ListViewBreadcrumbMixin, DetailViewBreadcrumbMixin

class CatalogIndexView(ListViewBreadcrumbMixin):
    template_name = 'catalog/index.html'
    model = Category
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = get_cart_data(self.request.user.id)
        return context
    
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
        context['cart'] = get_cart_data(self.request.user.id)
        return context
    
    def get_breadcrumbs(self):
        breadcrumbs = {reverse('catalog'): PAGE_NAMES['catalog']}
        if self.category.parent:
            linkss = []
            parent = self.category.parent
            while parent is not None:
                linkss.append(
                    (
                        reverse('category', kwargs={'slug': parent.slug}),
                        parent.name
                    )
                )
                parent = parent.parent
            for url, name in linkss[::-1]:
                breadcrumbs[url] = name
                #breadcrumbs.update({url: name}) # або так
        breadcrumbs.update({'current': self.category.name})
        return breadcrumbs

class ProductDetailView(DetailViewBreadcrumbMixin):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = get_cart_data(self.request.user.id)
        return context
    
    def get_breadcrumbs(self):
        breadcrumbs = {reverse('catalog'): PAGE_NAMES['catalog']}
        category = self.object.main_category()
        if category:
            if category.parent:
                linkss = []
                parent = category.parent
                while parent is not None:
                    linkss.append(
                        (
                            reverse('category', kwargs={'slug': parent.slug}),
                            parent.name
                        )
                    )
                    parent = parent.parent
                for url, name in linkss[::-1]:
                    breadcrumbs[url] = name
                    #breadcrumbs.update({url: name}) # або так
            breadcrumbs.update({reverse('category', kwargs={'slug': category.slug}): category.name})
        breadcrumbs.update({'current': self.object.name})
        return breadcrumbs

