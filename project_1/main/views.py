from multiprocessing import context
import re
from django.shortcuts import render, get_object_or_404, redirect

from pages import models

# Create your views here.
def main(request):
    context ={
        "alert" : False,
        "wrong" : False
    }
    return render(request, 'main.html', context)

# 로그인 했을 때 게시글 전체 확인하기
def database(request):
    articles = models.login.objects.all() 
    context = {
        'articles' : articles
    }

    return render(request, 'database.html', context)

# 게시글 상세보기
def detail(request, id):
    # filter와 get의 차이를 명확하게 알아야할듯
    article = models.login.objects.get(id = id)
    context = {
        "article" : article
    }
    return render(request, 'detail.html', context)

def delete(request,id):
    article = models.login.objects.get(id = id)
    article.delete()
    return render(request, 'database.html')
