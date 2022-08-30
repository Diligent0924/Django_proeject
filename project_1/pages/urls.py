from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.pages, name="pages"),
    path('', views.verify_pages, name = 'verify') # 중간과정으로 필요(html은 필요없음)
]