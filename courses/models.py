from django.db import models
from languages.models import Language


class Course(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title} (created on {self.created_at})'
