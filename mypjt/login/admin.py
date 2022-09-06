from django.contrib import admin
from . import models
# Register your models here.
class loginadmin(admin.ModelAdmin):
    list_display = ('verify_id','password')

admin.site.register(models.Login, loginadmin)