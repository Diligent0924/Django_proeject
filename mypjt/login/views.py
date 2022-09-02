from django.shortcuts import render, redirect
from . import models
# Create your views here.
def login(request):
    return render(request, 'login/login.html')

def verify(request):
    # id와 password를 가져온다.
    id = request.POST.get('id')
    password = request.POST.get('password')
    print(id, password)
    # model의 database에서 해당 id/password가 있는지 확인한다.
    database = models.Login.objects.filter(verify_id = id, password = password)
    print(database)
    if len(database) >= 1: # 만약 있다면
        return redirect("movies:index")
    else: # 없다면
        return redirect("login:login")

def joinmembership(request):
    return render(request, "login/joinmemebership.html")

def create(request):
    id = request.POST.get('id')
    password = request.POST.get('password')
    # 데이터베이스에 추가하기
    object = models.Login.objects.filter(verify_id = id) # 같은 아이디가 있는지 확인하기
    if len(object) >= 1: # 하나라도 있다면
        return redirect('login:joinmembership')
    else:
        real_object = models.Login(verify_id=id, password = password)
        real_object.save()
        return redirect('login:login')
