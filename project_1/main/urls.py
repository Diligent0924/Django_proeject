from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('database/', views.database, name='database'),
    path('database/<int:id>/', views.detail, name = 'detail'),
    path('delete/<int:id>', views.delete, name = 'delete'),
]