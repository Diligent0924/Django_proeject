from django.shortcuts import render, redirect
from . import models
from django.views.decorators.http import require_safe, require_http_methods, require_POST
# Create your views here.
@require_safe # GET인 요청에 대해서만 사용 => POST로 넘기면 405
def index(request):
    object = models.movies_info.objects.all() #데이터 변경이 없으므로 조회(GET)임
    context = {
        "articles" : object
    }
    return render(request, 'index.html', context)

# 추가하는 함수
from . import forms
def new(request):
    form = forms.NewForm() # forms에서 가져오는 방식
    context = {
        "form" : form,
    }
    return render(request, "new.html", context)

@require_http_methods(['GET','POST'])
# 생성한 데이터를 저장하는 함수
def create(request):
    if request.method == "POST": # 이미 만들어진 HTML FORM에서 작성해서 서버로 보낸다면
        form = forms.NewForm(request.POST) # Model에 있는 각각의 값을 호출한다.
        if form.is_valid(): # 전부 다 제대로 입력이 되었다면
            article = form.save() # 해당 자료를 저장한다. => Modelform이기 때문에 가능
            return redirect("movies:detail", article.id) # detail page로 가자
    else: # 입력해서 보내준 것이 아니라면 
        form = forms.NewForm() # 새로운 Form을 가져오기

    print(f"Error : {form.errors}")
    context = {
        "form" : form,
    }
    return render(request, "create.html", context) # create.html로 넘어가기

# 개별적으로 나타내는 것
def detail(request, id):
    article = models.movies_info.objects.get(id = id)
    print(article.title)
    context ={
        "article" : article
    }
    return render(request, "detail.html", context)

#업데이트
@require_http_methods(['GET','POST'])
def update(request, id):
    article = models.movies_info.objects.get(id=id)
    if request.method == "POST":
        form = forms.NewForm(request.POST, instance=article) 
        # instance : 
        if form.is_valid():
            form.save()
            return redirect("movies:index")
    else:
        form = forms.NewForm(instance=article)
    context = {
        'form' : form,
        'article' : article,
    }
    return render(request, 'update.html', context)

# 삭제함수
@require_POST # POST일 때만 사용하게끔 한다. => POST??? 
def delete(request, id):
    article = models.movies_info.objects.get(id = id)
    article.delete()
    return redirect('movies:index')