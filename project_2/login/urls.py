from django.urls import path, include
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login , name='login'),
    path('verify/', views.verify, name='verify'), # 반드시 다른 url을 만들어줘야한다.
]
