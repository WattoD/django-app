from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=16)
    code = models.CharField(max_length=2)
    rtl = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} [{self.code}]'