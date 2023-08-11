# Generated by Django 4.2.1 on 2023-08-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_image_product'),
        ('core', '0004_alter_page_options_productset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productset',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='product_sets', to='catalog.product', verbose_name='Товари'),
        ),
    ]