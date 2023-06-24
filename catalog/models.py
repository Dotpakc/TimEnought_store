from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.conf import settings

from mptt.models import MPTTModel, TreeForeignKey

from imagekit.models import ProcessedImageField
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
    
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        
    def __str__(self):
        return self.name