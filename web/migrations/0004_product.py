# Generated by Django 5.1.1 on 2024-10-16 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_workerprofile_interested_workerprofile_job_creator_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
