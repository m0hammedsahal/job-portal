# Generated by Django 5.1.1 on 2024-09-09 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.IntegerField(default=40),
        ),
    ]
