# Generated by Django 3.2.5 on 2021-08-06 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deladmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='adminLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deladmin.signup')),
            ],
        ),
    ]