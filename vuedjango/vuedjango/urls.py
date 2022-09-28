from django.conf.urls import include
from django.urls import re_path as url # router를 하기 위한 url을 뽑는 과정
from django.contrib import admin
from rest_framework import routers
from api.views import UsermodelSet

router = routers.DefaultRouter() 
router.register('User',UsermodelSet) # 뒤에 붙는 것:User, UsermodelSet:

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(router.urls)),
]