# Generated by Django 3.2.4 on 2021-08-05 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_is_sell_product_is_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
