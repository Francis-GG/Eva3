from django.shortcuts import render, redirect
from .models import Usuario
from django.http import HttpResponse
from urllib import response


# Create your views here.

def login(request):
    return render(request, 'login.html')

def validarUsuario (request):
    v_email=request.POST.get("email")
    v_password=request.POST.get("password")

    try:    
        usu=Usuario.objects.get(email=v_email, password=v_password)

        if usu:
            request.session['usuario'] = v_email
            return redirect('/productos/')
    except:
        return redirect('/login/')

def indexBack(request):
    if 'usuario' not in request.session:
        return redirect('/login/')
    return redirect('/productos/')