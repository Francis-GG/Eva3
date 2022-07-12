from django.shortcuts import render, redirect
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

'''
idProducto = models.IntegerField(primary_key=True, verbose_name="ID Producto")
    nombreProducto = models.CharField(max_length=100, verbose_name="Nombre Producto")
    precioProducto = models.IntegerField(max_length=9, verbose_name="Precio Producto")
    stockProducto = models.IntegerField(max_length=9, verbose_name="Stock Producto")
    nombreArchivo = models.CharField(max_length=256, verbose_name="Nombre Foto")
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, related_name='productos')   
''' 


def guardarProducto(request):
    
    v_idproducto=request.POST.get('idProducto')
    v_nombreproducto=request.POST.get('nombreProducto')
    v_precioproducto=request.POST.get('precioProducto')
    v_stockproducto=request.POST.get('stockProducto')
    v_nombrearchivo=request.POST.get('nombreArchivo')
    v_categoria=request.POST.get('categoria')

    nuevo=producto()
    nuevo.idProducto=v_idproducto
    nuevo.nombre=v_nombreproducto
    nuevo.precio=v_precioproducto
    nuevo.stock=v_stockproducto
    nuevo.nombreArchivo=v_nombrearchivo
    nuevo.categoria=v_categoria
    

    producto.save(nuevo)

    return render(request, 'controlproductos.html')
    
def eliminarProducto(request, p_idProducto):
    buscado=producto.objects.get(idProducto=p_idProducto)
    if(buscado):
        producto.delete(buscado)
        return redirect('/')

def buscarProducto(request, p_idProducto):
    buscado=producto.objects.get(idProducto=p_idProducto)
    datos={'producto': buscado}
    return render(request, 'modificar.html', datos)

def guardarProductoModificado(request):
    v_idproducto=request.POST.get('idProducto')
    v_nombreproducto=request.POST.get('nombreProducto')
    v_precioproducto=request.POST.get('precioProducto')
    v_stockproducto=request.POST.get('stockProducto')
    v_nombrearchivo=request.POST.get('nombreArchivo')
    v_categoria=request.POST.get('categoria')

    buscado=producto.objects.get(idProducto=v_idproducto)

    
    if(buscado):
        buscado.nombre=v_nombreproducto
        buscado.precio=v_precioproducto
        buscado.stock=v_stockproducto
        buscado.nombrearchivo=v_nombrearchivo
        buscado.categoria=v_categoria

        producto.save(buscado)
        return redirect('/')