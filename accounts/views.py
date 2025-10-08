from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from accounts.forms import LoginForm


def user_login (request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    form = LoginForm()
                    return render(request,'account/login.html',{'info':'Foydalanuvchi aktiv emas','form': form})
            else:
                form = LoginForm()
                return render(request,'account/login.html',{'info':'Login yoki parol xato kiritildi','form': form})
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

@login_required
def tadbir(request):
    return render(request, 'tadbir.html')


@login_required
def phone(request):
    return render(request, 'phone.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')