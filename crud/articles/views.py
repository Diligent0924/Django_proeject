from wsgiref.util import request_uri
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
    if not request.user.is_authenticated:
        return redirect("articles:home")
    
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # commit=False는 Form에서 값만 가져오고 실제 저장은 안되게끔 한다.
            same = ArticleModel.objects.filter(title = post.title)
            if len(same) >= 1:
                context = {
                    "same" : True,
                    "form" : form
                }
                return render(request, "articles/create.html", context)
            
            form.save()
            return redirect("articles:home")
    else:
        form = ArticleForm(initial={'username':request.user.username})
    context = {
        "form" : form
    }
    return render(request, "articles/create.html", context)

def delete(request, id):
    article = ArticleModel.objects.get(id = id)
    article.delete()
    return redirect("articles:home")

def myarticle(request):
    articles = ArticleModel.objects.filter(username = request.user.username)
    context = {
        'articles' : articles
    }
    
    return render(request, "articles/myarticle.html", context)