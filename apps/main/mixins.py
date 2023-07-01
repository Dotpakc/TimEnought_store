from django.db import models


class MetaTagMixin(models.Model):
    name = None
    meta_title = models.CharField(verbose_name='Мета заголовок', max_length=255, blank=True, null=True)
    meta_description = models.TextField(verbose_name='Мета опис', blank=True, null=True)
    meta_keywords = models.TextField(verbose_name='Мета ключові слова', blank=True, null=True)
    
    def get_meta_title(self):
        return self.meta_title or self.name # якщо meta_title не заповнений то повернеться name
    
    class Meta:
        abstract = True