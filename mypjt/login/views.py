from multiprocessing import context
from django.shortcuts import render, redirect
from . import models
from . import forms
# Create your views here.
def login(request):
    form = forms.LoginForm()
    context = {
        'form' : form
    }
    return render(request, 'login/login.html', context)

def verify(request):
    keys = request.POST.keys()
    print(keys)
    # id와 password를 가져온다.
    Dic = {}
    for key in keys:
        Dic[key] = request.POST.get(key)
    print(Dic['id'], Dic['password'])
    # model의 database에서 해당 id/password가 있는지 확인한다.
    database = models.Login.objects.filter(verify_id = Dic['id'], password = Dic['password'])
    print(database)
    if len(database) >= 1: # 만약 있다면
        return redirect("movies:index")
    else: # 없다면
        return redirect("login:login")

# 데이터베이스 자체를 조작해야하는 경우에는 MODEFORM으로 사용
def joinmembership(request):
    form = forms.plusForm()
    context = {
        "form" : form
    }
    return render(request, "login/joinmemebership.html", context)

def create(request):
    form = forms.plusForm(request.POST)
    print(form)
    if form.is_valid():
        form.save() # 그냥 해당 form을 해도 저장이 된다?
        return redirect('login:login')
    return redirect('login:joinmembership')

