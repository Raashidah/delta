# Generated by Django 3.2.5 on 2021-08-03 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='image',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.RemoveField(
            model_name='image',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='brand',
        ),
        migrations.DeleteModel(
            name='category',
        ),
        migrations.DeleteModel(
            name='image',
        ),
        migrations.DeleteModel(
            name='product',
        ),
    ]
