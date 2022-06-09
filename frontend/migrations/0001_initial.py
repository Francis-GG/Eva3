# Generated by Django 4.0.4 on 2022-06-09 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID Categoría')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID Producto')),
                ('nombreProducto', models.CharField(max_length=100, verbose_name='Nombre Producto')),
                ('precioProducto', models.IntegerField(max_length=9, verbose_name='Precio Producto')),
                ('stockProducto', models.IntegerField(max_length=9, verbose_name='Stock Producto')),
                ('nombreArchivo', models.CharField(max_length=256, verbose_name='Nombre Foto')),
            ],
        ),
    ]