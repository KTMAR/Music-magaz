# Generated by Django 3.2.7 on 2021-09-27 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicshop', '0004_alter_cart_final_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='musicshop.cart', verbose_name='Корзина'),
        ),
    ]