# Generated by Django 4.2.1 on 2023-06-17 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(verbose_name='Назва'),
        ),
    ]
