from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request,"appmyweb/home.html")

def tienda(request):
    return render(request,"appmyweb/tienda.html")

def servicios(request):
    return render(request,"appmyweb/servicios.html")

def contacto(request):
    return render(request,"appmyweb/contacto.html")
