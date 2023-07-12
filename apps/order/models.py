from django.db import models
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField

from apps.catalog.models import Product


# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    # quantity повино бути так 
    # в шаблоні використовуємо був варіан зверху 
    quantity = models.PositiveIntegerField(verbose_name='Кількість', default=1)
    user = models.ForeignKey(get_user_model(), verbose_name='Користувач', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.product.name} - {self.quantity}'
    
    
class Order(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name='Користувач', on_delete=models.CASCADE)
    total = models.PositiveIntegerField(verbose_name='Сума замовлення', default=0)
    first_name = models.CharField(verbose_name='Ім\'я', max_length=255)
    last_name = models.CharField(verbose_name='Прізвище', max_length=255)
    email = models.EmailField(verbose_name='Електронна пошта')
    phone = PhoneNumberField(verbose_name='Телефон')
    address = models.CharField(verbose_name='Адреса', max_length=255)
    comments = models.TextField(verbose_name='Коментарі', blank=True, null=True)
    created = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)    
    updated = models.DateTimeField(verbose_name='Дата оновлення', auto_now=True)
    paid = models.BooleanField(verbose_name='Оплачено', default=False)
    
    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
        
    def __str__(self):  
        return f'Замовлення №{self.id}'
        
        
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, verbose_name='Замовлення', related_name='products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name='Ціна', default=0)
    quantity = models.PositiveIntegerField(verbose_name='Кількість', default=1)
    
    def __str__(self):
        return f'{self.product.name} - {self.quantity}'
    
    class Meta:
        verbose_name = 'Товар замовлення'
        verbose_name_plural = 'Товари замовлення'