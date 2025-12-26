from django.db import models

# Create your models here.

class MovieInfo(models.Model):
    title = models.CharField(max_length=20)
    year = models.IntegerField(null=True, blank=True)
    summary = models.TextField()


class Director(models.Model):
    name=models.CharField(max_length=30)    

