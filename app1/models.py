from django.db import models

# Create your models here.

class Grabacion(models.Model):
    nombre = models.CharField(max_length=2000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    archivo= models.FileField(upload_to='grabacion/%Y/%m/%d/')
