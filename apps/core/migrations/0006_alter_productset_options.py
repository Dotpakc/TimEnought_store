# Generated by Django 4.2.1 on 2023-08-09 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_productset_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productset',
            options={'ordering': ('-sort',), 'verbose_name': 'Набір товарів', 'verbose_name_plural': 'Набори товарів'},
        ),
    ]
