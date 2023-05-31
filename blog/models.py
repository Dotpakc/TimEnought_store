from django.db import models

# Create your models here.
class Article(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='articles', default=1, verbose_name='Категория')
    tags = models.ManyToManyField('Tag', related_name='articles', verbose_name='Теги')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='URL')
    content_preview = models.TextField(verbose_name='Превью статьи')
    content = models.TextField(verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
    
    
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва тегу')
    slug = models.SlugField(verbose_name='URL', default='')
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255, verbose_name='Ім\'я')
    email = models.EmailField(verbose_name='Email')
    content = models.TextField(verbose_name='Коментар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')

    def __str__(self):
        return f'{self.article.title} - {self.content}'
        