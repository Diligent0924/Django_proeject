from django.db import models

# Create your models here.
class Login(models.Model):
    info = models.BigAutoField(primary_key=True)
    verify_id = models.CharField(max_length=20)
    password = models.CharField(max_length=20)