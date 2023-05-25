from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    intro = models.TextField()
    body = models.TextField()
    image = models.URLField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
        
    

    class Meta: # це для того, щоб в адмінці відображалося "Пости" замість "Posts"
        verbose_name = "Пост"
        verbose_name_plural = "Пости"

    def __str__(self): # це для того, щоб в адмінці відображалося назва поста замість "Post object (1)"
        return self.title

