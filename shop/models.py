from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(verbose_name='Категорія',max_length=255)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class Product(models.Model):
    catagory = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(verbose_name='Назва',max_length=255)
    slug = models.SlugField(max_length=255)
    description = RichTextField(verbose_name='Контент')
    price = models.DecimalField(verbose_name='Ціна',max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name
    