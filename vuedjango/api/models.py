from django.db import models

# Create your models here.
class Usermodel(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)