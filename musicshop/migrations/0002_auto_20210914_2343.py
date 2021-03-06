# Generated by Django 3.2.7 on 2021-09-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='track',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='musicshop.CartProduct', verbose_name='Продукты для корзины'),
        ),
    ]
