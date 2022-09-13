from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('create/', views.create, name='create'),
    path('<int:id>/detail/', views.detail, name='detail'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('myarticle/', views.myarticle, name= 'my_article'),
]
