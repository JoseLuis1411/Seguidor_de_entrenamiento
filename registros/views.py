from django.shortcuts import render, redirect
from .forms import crearUsuario, LoginForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def homeR(request):
    return render(request, "registros/home.html")

def logueo(request):
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    return render(request, 'registration/login.html', {"form": form})

def cerrar(request):
     logout(request)
     return redirect("home")

def registro(request):
    if request.method=="POST":
        crear=crearUsuario(request.POST)
        if crear.is_valid():
            user = crear.save()
            login(request, user)
            return redirect ("login")
        else:
            return render(request, "registration/register.html", {"form": crear})
    crear=crearUsuario()
    return render(request, "registration/register.html", {'form':crear})