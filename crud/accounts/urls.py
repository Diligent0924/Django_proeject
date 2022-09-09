from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('index/', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('<int:id>/update/', views.update, name = 'update'),
    path('<int:id>/delete/', views.delete, name = 'delete'),
    path('logout/', views.logout, name = 'logout'),
    path('<int:id>/password/', views.change_password, name = 'change_password'),
]
