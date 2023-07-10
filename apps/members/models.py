from django.db import models
#AbstractUser - це модель користувача, яка містить всі необхідні поля для роботи з користувачами
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

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
    