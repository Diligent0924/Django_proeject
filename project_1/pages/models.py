from django.db import models

# Create your models here.
class login(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20,default='1111')
    email = models.EmailField(default='00000@naver.com')
    grade = models.CharField(max_length=10, default = 'IM')
    age = models.IntegerField()
    telephone = models.IntegerField()
    descriptn = models.TextField()
    
    def __Str__(self):
        return [self.id, self.password, self.grade, self.name, self.descript]
    