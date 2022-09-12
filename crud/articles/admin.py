from django.contrib import admin
from . import models
# Register your models here.
class articleadmin(admin.ModelAdmin):
    list_display = ('username','title','release_date','update_date')

admin.site.register(models.ArticleModel, articleadmin)
