# Generated by Django 3.2.3 on 2021-10-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deladmin', '0007_remove_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.CharField(max_length=5),
        ),
    ]