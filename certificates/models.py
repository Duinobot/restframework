from tkinter import CASCADE
from django.db import models
from django.conf import settings
from users.models import CustomUser
# Create your models here.
class Certificate(models.Model):
    content = models.TextField(null=True)
    imei = models.IntegerField()
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.imei)
