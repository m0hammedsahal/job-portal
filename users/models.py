from django.db import models
from django.contrib.auth.models import User


class JobCreator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_job_creator"
        verbose_name = "job_creator"
        verbose_name_plural = "job_creators"
        ordering = ["-id"]


    def __str__(self):
        return self.user.username

