from django.shortcuts import render
from .models import producto, categoria

# Create your views here.

def index(request):
    return render(request, 'main.html')

def bored(request):
    return render(request, 'bored.html')

def productos(request):
    categorias=categoria.objects.all()
    productos = producto.objects.all()
    datos = {'productos': productos, 'categorias': categorias}
    return render(request, 'productos.html', datos)

def pago (request):
    return render(request, 'pago.html')

def registro (request):
    return render(request, 'registro.html')

def historial (request):
    return render(request, 'historial.html')

def carro (request):
    return render(request, 'carro.html')