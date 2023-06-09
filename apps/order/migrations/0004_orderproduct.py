# Generated by Django 4.2.1 on 2023-07-12 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_category_meta_description_category_meta_keywords_and_more'),
        ('order', '0003_alter_order_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Ціна')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Кількість')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='order.order', verbose_name='Замовлення')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар замовлення',
                'verbose_name_plural': 'Товари замовлення',
            },
        ),
    ]
