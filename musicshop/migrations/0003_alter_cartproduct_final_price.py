# Generated by Django 3.2.7 on 2021-09-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicshop', '0002_auto_20210914_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='final_price',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True, verbose_name='Общая цена'),
        ),
    ]
