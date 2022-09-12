from django.shortcuts import render, redirect
from .models import ArticleModel
from .forms import ArticleForm

# Create your views here.
def home(request):
    articles = ArticleModel.objects.all()
    context = {
        "articles" : articles
    }
    return render(request, 'articles/home.html', context)

def detail(request, id):
    article = ArticleModel.objects.get(id = id)
    context = {
        "article" : article
    }
    return render(request, "articles/detail.html", context)
    
def create(request):
    if request.method() == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:home")
    else:
        form = ArticleForm()
    context = {
        "form" : form
    }
    return render(request, "articles/create.html", context)