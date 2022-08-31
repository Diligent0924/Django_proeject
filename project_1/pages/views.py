from multiprocessing import context
from django.shortcuts import render
from . import database
from . import models
dic = database.dic # 바깥쪽에 아예 DataBase를 빼놓음 => 추후 연결
# Create your views here.
def verify_pages(request): # 이름 / 비밀번호가 같은지만 확인하는 구조이므로 html 따로 필요 X
    # dic = database.dic # 임시 데이터베이스 => 이후 MySQL로 변경 예정
    name = request.GET.get('name') # form 데이터 받기
    password = request.GET.get('password') 
    print(name, password)
    # print(models.login.objects.values())
    # print(models.login.objects.values()[0])
    # print(len(models.login.objects.values()))
    for i in range(len(models.login.objects.values())):
        object = models.login.objects.values()[i]
        print(object)
        if object['name'] == name and object['password'] == password:
            return pages(request, object['id'])
    # 만약 틀린다면 True로 변경해줘라
    context = {
        "alert" : True
    }
    return render(request, "main.html", context) # 다른 APP에 있는 templates도 가져올 수 있음

def pages(request, id):
    for i in range(len(models.login.objects.values())):
        object = models.login.objects.values()[i]
        if object["id"] == id:
            context = {
            "id" : object['id'],
            "name" : object['name'],
            "age" : object['age'],
            "descript" : object['descript'],
            "grade" : object['grade'],
            }
            return render(request, "pages.html", context)