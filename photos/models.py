from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
