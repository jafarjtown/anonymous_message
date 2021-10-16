from django.db import models

# Create your models here.


class Messages(models.Model):
    messages = models.ManyToManyField('M', blank=True)
    link1 = models.CharField(max_length=100)
    link2 = models.CharField(max_length=100)
    timestamp = models.DateTimeField( auto_now_add=True)

class M(models.Model):
    message = models.TextField()
    timestamp = models.DateTimeField( auto_now_add=True)