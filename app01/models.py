from django.db import models

# Create your models here.

class Test(models.Model):
    node = models.TextField()
    pinglun = models.TextField(null=True)