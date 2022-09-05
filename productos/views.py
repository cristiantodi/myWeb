from re import A
from django.shortcuts import render
from productos.models import Articulo, Categoria

# Create your views here.

def productos(request):   
    articulos=Articulo.objects.all()
    return render(request, "productos/productos.html",{"articulos":articulos})

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    articulos=Articulo.objects.filter(categorias=categoria)
    return render(request, 'productos/categoria.html',{'categoria':categoria, "articulos":articulos})