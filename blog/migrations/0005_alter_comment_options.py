# Generated by Django 4.2.1 on 2023-05-31 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_article_options_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at'], 'verbose_name': 'Коментар', 'verbose_name_plural': 'Коментарі'},
        ),
    ]
