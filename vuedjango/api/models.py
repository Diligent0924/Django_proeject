from django.db import models

# Create your models here.
class Usermodel(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=15)

class Articlemodel(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()