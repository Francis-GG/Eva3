from django.shortcuts import render, redirect

from backend.forms import UsuarioForm
from .models import Usuario
from django.http import HttpResponse
from urllib import response
from rest_framework import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



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

def form_usuario(request):

    datos = {
        'form': UsuarioForm()
    }

    if request.method == 'POST' :
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardados correctamente'

    return render(request, 'registro-usuarios.html', datos)