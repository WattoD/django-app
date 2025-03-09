from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} (created on {self.created_at})'
