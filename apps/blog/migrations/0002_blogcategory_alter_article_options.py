# Generated by Django 4.2.1 on 2023-05-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Категорія блогу',
                'verbose_name_plural': 'Категорії блогу',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-сreated_at'], 'verbose_name': 'Стаття', 'verbose_name_plural': 'Статті'},
        ),
    ]
