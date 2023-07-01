# Generated by Django 4.2.1 on 2023-07-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='Мета опис'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_keywords',
            field=models.TextField(blank=True, null=True, verbose_name='Мета ключові слова'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Мета заголовок'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='Мета опис'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_keywords',
            field=models.TextField(blank=True, null=True, verbose_name='Мета ключові слова'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Мета заголовок'),
        ),
    ]
