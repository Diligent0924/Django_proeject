from platform import release
from urllib import request
from django.db import models

# Create your models here.
class ArticleModel(models.Model):
    variety_1 = (
              ('Backjoon', 'Backjoon'),
              ('SWEA', 'SWEA'),
              ('Programmers', 'Programmers'),
              ('else', 'else'),
    )
    username = models.CharField(max_length=30)
    title = models.CharField(max_length= 30)
    content = models.TextField()
    release_date = models.DateField(auto_now = True)
    update_date = models.DateField(auto_now_add= True)
    variety = models.CharField(max_length=30, choices=variety_1)

class CommentModel(models.Model):
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, default="Please write")
    comment = models.TextField()
    create_at = models.DateField(auto_now = True)
    update_at = models.DateField(auto_now_add=True)