# Generated by Django 4.0.4 on 2022-05-03 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caliza', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
