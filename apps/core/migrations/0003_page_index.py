# Generated by Django 4.2.1 on 2023-07-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_page_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='index',
            field=models.IntegerField(blank=True, default=-1, verbose_name='Індекс сортування'),
        ),
    ]
