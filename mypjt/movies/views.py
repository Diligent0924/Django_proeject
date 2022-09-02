from audioop import reverse
from multiprocessing import context
from django.shortcuts import render, redirect
from . import models
# Create your views here.
def index(request):
    object = models.movies_info.objects.all()
    context = {
        "articles" : object
    }
    return render(request, 'index.html', context)

# 추가하는 함수
def new(request):
    genre = ["코미디","호러","드라마","스릴러", "액션", "판타지"]
    context = {
        "genres" : genre,
    }
    return render(request, "new.html", context)

# 생성한 데이터를 저장하는 함수
def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    article = models.movies_info(title = title, audience = audience, release = release_date, genre = genre, score = score, poster_url = poster_url, description = description)
    article.save()
    return redirect("movies:detail", article.id)

# 개별적으로 나타내는 것
def detail(request, id):
    article = models.movies_info.objects.get(id = id)
    context ={
        "article" : article
    }
    return render(request, "detail.html", context)

# 수정하기
def edit(request, id):
    article = models.movies_info.objects.get(id = id)
    genre = ["코미디","호러","드라마","스릴러", "액션", "판타지"]
    context = {
        "article" : article,
        'genres' : genre
    }
    print(article.title)
    return render(request, "edit.html", context)

# 업데이트
def update(request, id):
    article = models.movies_info.objects.get(id = id)
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    article = models.movies_info(id = id, title = title, audience = audience, release = release_date, genre = genre, score = score, poster_url = poster_url, description = description)
    article.save()
    return redirect("movies:index")

# 삭제함수
def delete(request, id):
    article = models.movies_info.objects.get(id = id)
    article.delete()

    return redirect('movies:index')