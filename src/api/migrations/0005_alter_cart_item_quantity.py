# Generated by Django 4.1.5 on 2023-02-06 07:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_cart_item_cart_alter_cart_item_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_item',
            name='quantity',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
