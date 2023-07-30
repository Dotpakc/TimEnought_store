from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

from .mixins import MetaTagMixin
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