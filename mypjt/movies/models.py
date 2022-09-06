from django.db import models

# Create your models here.
class movies_info(models.Model):
    genre_list = [("공포", "공포"),("스릴러", "스릴러"),("액션", "액션"),("드라마", "드라마")]
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release = models.DateField()
    genre = models.CharField(max_length=30, choices=genre_list)
    score = models.FloatField()
    poster_url = models.TextField()
    sub_description = models.TextField(default='aa')
    description = models.TextField()