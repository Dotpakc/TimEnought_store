from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

from .mixins import MetaTagMixin
from apps.catalog.models import Product
# Create your models here.

class Page(MetaTagMixin):
    name = models.CharField(verbose_name='Назва', max_length=255)
    slug = models.SlugField(verbose_name='URL', max_length=255, unique=True)
    content = RichTextField(verbose_name='Контент', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активна', default=True)
    index = models.IntegerField(verbose_name='Індекс сортування', default=-1, blank=True)
        
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('page', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Сторінка'
        verbose_name_plural = 'Сторінки'
        ordering = ['index', 'name']
        
class ProductSet(models.Model):
    name = models.CharField(verbose_name='Назва', max_length=255)
    products = models.ManyToManyField(Product, verbose_name='Товари', related_name='product_sets', blank=True, null=True)
    sort = models.IntegerField(verbose_name='Індекс сортування', default=-1, blank=True)
    is_active = models.BooleanField(verbose_name='Активна', default=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Набір товарів'
        verbose_name_plural = 'Набори товарів'
        ordering = ('-sort',)
        
