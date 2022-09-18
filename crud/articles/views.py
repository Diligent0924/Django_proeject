from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from .models import ArticleModel, CommentModel
from .forms import ArticleForm, CommentForm

# Create your views here.
def home(request):
    articles = ArticleModel.objects.all()
    comments = CommentModel.objects.all()
    comments_dic = {}
    for article in articles:
        comments = CommentModel.objects.filter(article = article)
        comments_dic[article.id] = len(comments)
        print(comments_dic[article.id])
        
    context = {
        "articles" : articles,
        "comments_dic" : comments_dic,
    }
    return render(request, 'articles/home.html', context)

# 상세 페이지
def detail(request, id):
    article = ArticleModel.objects.get(id = id)
    article.visited = article.visited + 1
    article.save() # 방문수를 계산하기 위해서 조회수를 저장해둔다.
    print(article.visited)
    comment_articles = CommentModel.objects.filter(article = article)
    if request.user.is_authenticated and request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.username = request.user.username
            comment.save()
            return redirect("articles:detail", article.id)
    else:
        comment_form = CommentForm()
    context = {
        "article" : article,
        "comment_form" : comment_form,
        "comment_articles" : comment_articles,
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

# 개인게시판
def myarticle(request):
    articles = ArticleModel.objects.filter(username = request.user.username)
    context = {
        'articles' : articles
    }
    
    return render(request, "articles/myarticle.html", context)

def comment_delete(request, id):
    comment = CommentModel.objects.get(id = id)
    comment.delete()
    return redirect("articles:detail", comment.article.id) # comment.article을 외부키로 뒀기 때문에 같이 삭제되는 것 같다.

# 여기서부터는 종류별로 페이지 호출하는 함수
def else_board(request):
    articles = ArticleModel.objects.filter(variety = "else")
    context = {
        "articles" : articles
    }
    return render(request, "articles/else_board.html", context)

def Backjoon_board(request):
    articles = ArticleModel.objects.filter(variety = "Backjoon")
    context = {
        "articles" : articles
    }
    return render(request, "articles/Backjoon_board.html", context)

def SWEA_board(request):
    articles = ArticleModel.objects.filter(variety = "SWEA")
    context = {
        "articles" : articles
    }
    return render(request, "articles/SWEA_board.html", context)

def Programmers_board(request):
    articles = ArticleModel.objects.filter(variety = "Programmers")
    context = {
        "articles" : articles
    }
    return render(request, "articles/Programmers_board.html", context)
