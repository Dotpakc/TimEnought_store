from django.db import models
#AbstractUser - це модель користувача, яка містить всі необхідні поля для роботи з користувачами
from django.contrib.auth.models import AbstractUser
from django.shortcuts import redirect
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

from django.conf import settings

DOMAIN =  settings.DOMAIN

# Create your models here.
# TODO ДОРОБИТИ МОДЕЛЬ КОРИСТУВАЧА
class UserProfile(AbstractUser):
    phone = PhoneNumberField(verbose_name='Телефон', blank=True, null=True)
    address = models.CharField(verbose_name='Адреса', max_length=255, blank=True, null=True)
    image = ProcessedImageField(
        verbose_name='Зображення',
        upload_to='users',
        processors=[],
        format='JPEG',
        options={'quality': 100},
        null=True
        )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 70}
    )
    referal = models.ForeignKey('self', verbose_name='Реферал', on_delete=models.SET_NULL, blank=True, null=True, related_name='referals')
    balance = models.DecimalField(verbose_name='Баланс',default=0, max_digits=10, decimal_places=2)
    
    def get_referal_link(self):
        # return f'http://{DOMAIN}{redirect("signup")}?ref={self.username}'
        return f'http://{DOMAIN}/members/signup/?ref={self.username}'
    
