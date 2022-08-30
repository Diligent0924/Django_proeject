from django.shortcuts import render
from . import database
dic = database.dic # 바깥쪽에 아예 DataBase를 빼놓음 => 추후 연결
# Create your views here.
def verify_pages(request): # 이름 / 비밀번호가 같은지만 확인하는 구조이므로 html 따로 필요 X
    # dic = database.dic # 임시 데이터베이스 => 이후 MySQL로 변경 예정
    name = request.GET.get('name') # form 데이터 받기
    password = request.GET.get('password') 
    print(name, password)
    for id in dic:
        if dic[id]['name'] == name and dic[id]['password'] == password:
            return pages(request, id)
    return render(request, "main.html") # 다른 APP에 있는 templates도 가져올 수 있음

def pages(request, id):
    # dic = database.dic
    context = {
        "id" : id,
        "name" : dic[id]['name'],
        "age" : dic[id]['age'],
        "text" : dic[id]['text'],
    }
    return render(request, "pages.html", context)