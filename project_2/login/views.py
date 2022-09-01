from django.shortcuts import render
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
        return render(request, "main/mainpages.html")
    else: # 없다면
        return render(request, "login/login.html")