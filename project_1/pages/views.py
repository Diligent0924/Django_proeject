from multiprocessing import context
import re
from django.shortcuts import render
from . import models

# Create your views here.
def verify_pages(request): # 이름 / 비밀번호가 같은지만 확인하는 구조이므로 html 따로 필요 X
    # dic = database.dic # 임시 데이터베이스 => 이후 MySQL로 변경 예정
    name = request.POST.get('name') # form 데이터 받기
    password = request.POST.get('password') 
    print(name, password)
    print(models.login.objects.all())
    # print(models.login.objects.values())
    object = models.login.objects.filter(name = name, password = password)
    print(object.values())
    if len(object) != 0:
        return pages(request, object.values()[0]['id'])

    context = {
        "wrong" : True,
        "w_name" : name,
        "w_password" : password,
    }
    print(context)
    return render(request, "main.html", context) # 다른 APP에 있는 templates도 가져올 수 있음

def pages(request, id):
    for i in range(len(models.login.objects.values())):
        object = models.login.objects.values()[i]
        if object["id"] == id:
            context = {
            "name" : object['name'],
            "age" : object['age'],
            "descript" : object['descript'],
            "grade" : object['grade'],
            "email" : object['email'],
            "telephone" : object['telephone'],
            }
            return render(request, "pages.html", context)

def info(request):
    return render(request, 'info.html')

# 회원가입을 저장해 주는곳 => return은 따로 필요 없다.
def joinmembership(request):
    # 만약 아무것도 넣지 않는다면 ''인가? 아니면 None인가?
    name = request.POST.get('name')
    password = request.POST.get('password')
    email = request.POST.get('email')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    telephone = request.POST.get('telephone')
    descript = request.POST.get('descript')
    object_1 = models.login.objects.filter(name = name)
    print(len(object_1))
    if len(object_1) >= 1:
        context = {
            "name" : name,
            "same_name" : 1
        }
        return render(request, 'info.html', context)
    # 이외의 것을 사용
    object = models.login(name=name, password=password,email=email,grade=grade,age=age,telephone=telephone,descript=descript)
    object.save()
    return render(request, 'main.html')
    