from django.db import models

from django.contrib.auth.models import User

from apps.catalog.models import Product


# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    # quantity повино бути так 
    # в шаблоні використовуємо був варіан зверху 
    quantity = models.PositiveIntegerField(verbose_name='Кількість', default=1)
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.product.name} - {self.quantity}'