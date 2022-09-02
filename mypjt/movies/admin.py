from django.contrib import admin
from . import models
# Register your models here.
class movieadmin(admin.ModelAdmin):
    list_display = ('title','audience','release','genre','score')

admin.site.register(models.movies_info, movieadmin)