import os

from django.db import models
from PIL import Image

# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(verbose_name="Назва", max_length=255)
    photo = models.ImageField(verbose_name="Фото", upload_to="blog_category_photo", blank=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.photo:
            image = Image.open(self.photo.path)
            if image.height > 300 or image.width > 300:
                resize = (300, 300)
                image.thumbnail(resize)
                image.save(self.photo.path)
    
    def delete(self, *args, **kwargs):
        if self.photo:
            if os.path.isfile(self.photo.path):
                os.remove(self.photo.path)
            self.photo.delete()
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категорія блогу"
        verbose_name_plural = "Категорії блогу"
        ordering = ["name"]

class Tag(models.Model):
    name = models.CharField(verbose_name="Назва", max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["name"]

class Article(models.Model):
    сategory = models.ForeignKey(BlogCategory, verbose_name="Категорія", on_delete=models.SET_NULL, null=True, related_name="articles")
    tags = models.ManyToManyField(Tag, verbose_name="Теги", blank=True)
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    text_preview = models.TextField(verbose_name="Текст-превью")
    text = models.TextField(verbose_name="Текст статьи")
    сreated_at = models.DateTimeField(verbose_name="Дата створення", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата оновлення", auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"
        ordering = ["-сreated_at"]