from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm


# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('vans')
        else:
            messages.success(request,"Невалидна електронска адреса или лозинка! Пробај повторно")
            return redirect('login')
    else:
        return render(request,'authentication/login.html', {})

def logout_user(request):
    messages.success(request,"Успешно одјавен!")
    logout(request)
    return redirect('login')

def signin_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data[username]
            password = form.changed_data[password]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"Успешна регистрација!")
        return redirect('login')

    else:
        
        form = RegisterForm()
        return render(request, 'authentication/sign_in.html',{'form':form,})