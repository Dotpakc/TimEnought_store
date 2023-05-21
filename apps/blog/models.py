from django.db import models

# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(verbose_name="Назва", max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категорія блогу"
        verbose_name_plural = "Категорії блогу"
        ordering = ["name"]

class Article(models.Model):
    сategory = models.ForeignKey(BlogCategory, verbose_name="Категорія", on_delete=models.SET_NULL, null=True)
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