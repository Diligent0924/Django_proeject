from django.shortcuts import render
from .models import ArticleModel

# Create your views here.
def home(request):
    articles = ArticleModel.objects.all()
    context = {
        "articles" : articles
    }
    return render(request, 'articles/home.html', context)