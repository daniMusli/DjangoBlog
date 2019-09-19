from django.shortcuts import render,redirect
from .forms import loginForm,registerForm
from django.contrib.auth import authenticate ,login,logout
# Create your views here.

def login_view(request):
    form = loginForm(request.POST or None)
    if form.is_valid():
        kullanici = form.cleaned_data.get('username')
        parola = form.cleaned_data.get('password')
        dogruluk = authenticate(username=kullanici , password=parola)
        if dogruluk is not None:
           login(request,dogruluk)
           return redirect('home')

    return render(request,'hesaplar/giris.html',{'form':form,'title':'Giriş Yap'})


def register_view(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
       user = form.save(commit=False)
       password = form.cleaned_data.get('password1')
       user.set_password(password)
       user.save()
       new_user = authenticate(username=user.username ,password=password)
       login(request,new_user)
       return redirect('home')
    return render(request,'hesaplar/giris.html',{'form':form, 'title':'Üye Ol'})


def cikis_view(request):
    logout(request)
    return redirect('home')
