# Generated by Django 5.1.1 on 2024-09-11 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('web', '0002_jobposting_job_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerprofile',
            name='interested',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workerprofile',
            name='job_creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.jobcreator'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workerprofile',
            name='rejectd',
            field=models.BooleanField(default=False),
        ),
    ]
