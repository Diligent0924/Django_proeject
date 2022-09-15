from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('create/', views.create, name='create'),
    path('<int:id>/detail/', views.detail, name='detail'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('myarticle/', views.myarticle, name= 'my_article'),
    path('<int:id>/comment_delete', views.comment_delete, name = 'comment_delete'),
    path('else_board/', views.else_board, name = 'else_board'),
    path('Backjoon_board/', views.Backjoon_board, name = 'Backjoon_board'),
    path('SWEA_board/', views.SWEA_board, name = 'SWEA_board'),
    path('Programmers_board/', views.Programmers_board, name = 'Programmers_board'),
]
