from django.contrib.admin import display
from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.conf import settings

from mptt.models import MPTTModel, TreeForeignKey

from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill

from ckeditor.fields import RichTextField

MEDIA_ROOT = settings.MEDIA_ROOT


class Category(MPTTModel):
    name = models.CharField(verbose_name='Назва', max_length=255)
    slug = models.SlugField(verbose_name='URL', max_length=255, unique=True)
    description = models.TextField(verbose_name='Опис', blank=True, null=True)
    parent = TreeForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='child',
        blank=True,
        null=True
    )
    image = ProcessedImageField(
        verbose_name='Зображення',
        upload_to='category/',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 70},
        blank=True,# поле не обов'язкове але може бути заповнене default='no_image.jpg',
        null=True, # поле може бути пустим
    )
    
    def __str__(self):
        full_path = [self.name]
        parent = self.parent
        while parent is not None:
            full_path.append(parent.name)
            parent = parent.parent
        return ' -> '.join(full_path[::-1])
    
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})
    
    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="70">')
    
    # Назва колонки в адмінці
    image_tag_thumbnail.short_description = 'Зображення'
    image_tag_thumbnail.allow_tags = True 
    
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}">')
    
    image_tag.short_description = 'Зображення'
    image_tag.allow_tags = True
    
    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        
        
class Product(models.Model):
    name = models.CharField(verbose_name='Назва', max_length=255)
    description = RichTextField(verbose_name='Опис', blank=True, null=True)
    quantity = models.PositiveIntegerField(verbose_name='Кількість', default=0)
    price = models.DecimalField(verbose_name='Ціна', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата оновлення', auto_now=True)
    category = models.ManyToManyField(
        to=Category,
        verbose_name='Категорії',
        through='ProductCategory',
        related_name='products',
        blank=True        
    )
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        
    def __str__(self):
        return self.name
    
    def images(self):
        return Image.objects.filter(product=self.id)
    
    def main_image(self):
        image = Image.objects.filter(product=self.id, is_main=True)
        if image:
            return image
        return self.images().first()
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.id})
    
    
    
class ProductCategory(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категорія', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основна', default=False)
    
    def __str__(self):
        return f'{self.product.name} - {self.category.name}'
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_main:
            ProductCategory.objects.filter(product=self.product, is_main=True).update(is_main=False)
        super().save(force_insert, force_update, using, update_fields)
        
    class Meta:
        verbose_name = 'Категорія товару'
        verbose_name_plural = 'Категорії товарів'
        

class Image(models.Model):
    image = ProcessedImageField(
        verbose_name='Зображення',
        upload_to='catalog/product/',
        processors=[],
        format='JPEG',
        options={'quality': 100},
        null=True
        )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 200)],
        format='JPEG',
        options={'quality': 70}
    )
    product = models.ForeignKey(
        to=Product,
        verbose_name='Товар',
        on_delete=models.CASCADE,
        related_name='images'
    )
    is_main = models.BooleanField(verbose_name='Основне', default=False)
    
    @display(description='Зображення')
    def image_tag_thumbnail(self):
        if self.image:
            if not self.image_thumbnail:
                Image.objects.get(id=self.id)
            return mark_safe(f'<img src="{self.image_thumbnail.url}" height="70">')
        
    @display(description='Зображення')
    def image_tag(self):
        if self.image:
            if not self.image_thumbnail:
                Image.objects.get(id=self.id)
            return mark_safe(f'<img src="{self.image_thumbnail.url}">')