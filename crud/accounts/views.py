import re
from django.shortcuts import render, redirect
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout # 실제 세션을 만드는 함수

# Create your views here.
def login(request): 
    if request.user.is_authenticated:
        return redirect("accounts:index")

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("articles:home")
    else:
        form = AuthenticationForm()
    context = {
        "form" : form
    }
    return render(request, 'accounts/login.html', context)

def index(request):
    database = User.objects.all()  # 쿼리셋
    print(request.user)
    context = {
        "database" : database
    }
    return render(request, 'accounts/index.html', context)

def create(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        "form" : form
    }
    return render(request, 'accounts/create.html', context)

def update(request, id):
    if request.method == "POST":
        if request.user.is_superuser == 1:
            user = User.objects.get(id=id)
        if request.user.is_superuser == 0:
            user = request.user
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect("accounts:index")
    else:
        if request.user.is_superuser == 1:
            user = User.objects.get(id=id)
        if request.user.is_superuser == 0:
            user = request.user
        form = CustomUserChangeForm(instance=user)
    context = {
        'form' : form
    }

    return render(request, 'accounts/update.html', context)

def delete(request,id):
    if request.user.is_superuser == 1:
        user = User.objects.get(id=id)
    if request.user.is_superuser == 0:
        user = request.user
    user.delete()
    auth_logout(request) # 세션 자체를 없애고 싶을 때
    return redirect('accounts:login')

def logout(request):
    auth_logout(request)
    return redirect('articles:home')

def change_password(request, id):
    if request.user.is_superuser == 1:
        user = User.objects.get(id=id)
    if request.user.is_superuser == 0:
        user = request.user

    if request.method == "POST":
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            # update_session_auth_hash(request, form.user) # 로그인상태를 유지하는 상태
        return redirect('accounts:index')
    else:
        form = PasswordChangeForm(user)
        id = id
    context = {
        "form" : form,
        "id" : id
    }
    return render(request, 'accounts/change_password.html', context)