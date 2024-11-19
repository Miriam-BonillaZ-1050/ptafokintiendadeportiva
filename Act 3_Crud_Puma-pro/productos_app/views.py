from django.shortcuts import render, redirect
from .models import Productos
# Create your views here.

def inicio_vista(request):
    losproductos=Productos.objects.all()
    return render(request, 'gestionarProductos.html',{'misproductos':losproductos})

def registrarProductos(request):
    id_productos = request.POST["num_id_productos"]
    nombre_p = request.POST["txt_nombre_productos"]
    descripcion = request.POST["txt_descripcion_productos"]
    stock = request.POST["num_stock_productos"]
    precio = request.POST["num_precio_productos"]
    categoria = request.POST["txt_categoria_productos"]

    guardarProductos = Productos.objects.create(id_productos=id_productos,nombre_p=nombre_p,
    descripcion=descripcion,stock=stock,precio=precio,categoria=categoria)
    return redirect('/')

def seleccionarProductos(request, id_productos):
    productos = Productos.objects.get(id_productos=id_productos)
    return render(request, "editarProductos.html",{"misproductos":productos})

def editarProductos(request):
    id_productos = request.POST["num_id_productos"]
    nombre_p = request.POST["txt_nombre_productos"]
    descripcion = request.POST["txt_descripcion_productos"]
    stock = request.POST["num_stock_productos"]
    precio = request.POST["num_precio_productos"]
    categoria = request.POST["txt_categoria_productos"]
    productos=Productos.objects.get(id_productos=id_productos)
    productos.nombre_p=nombre_p
    productos.descripcion=descripcion
    productos.stock=stock
    productos.precio=precio
    productos.categoria=categoria
    productos.save()
    return redirect('/')

def borrarProductos(request, id_productos):
    productos=Productos.objects.get(id_productos=id_productos)
    productos.delete()
    return redirect("/")