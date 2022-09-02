from django.db import models

# Create your models here.
class movies_info(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    sub_description = models.TextField(default='aa')
    description = models.TextField()