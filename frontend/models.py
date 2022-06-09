from tabnanny import verbose
from django.db import models

# Create your models here.

class categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="ID Categoría")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre Categoría")

def __str__(self):
    return self.nombreCategoria

class producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="ID Producto")
    nombreProducto = models.CharField(max_length=100, verbose_name="Nombre Producto")
    precioProducto = models.IntegerField(max_length=9, verbose_name="Precio Producto")
    stockProducto = models.IntegerField(max_length=9, verbose_name="Stock Producto")
    nombreArchivo = models.CharField(max_length=256, verbose_name="Nombre Foto")
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, related_name='productos')

def __str__(self):
    return self.nombreProducto
