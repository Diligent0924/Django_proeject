from django.db import models

# Create your models here.
class login(models.Model):
    id = models.IntegerField(primary_key=True)
    grade = models.CharField(max_length=10, default = 'IM')
    password = models.CharField(max_length=20,default='1111')
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    descript = models.TextField()
    
    def __Str__(self):
        return [self.id, self.password, self.grade, self.name, self.descript]
    