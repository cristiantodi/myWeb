from django.shortcuts import render
from appmyweb.models import TextoDetalle

from carro.carro import Carro

# Create your views here.

def home(request):
    carro=Carro(request)
    detalle=TextoDetalle.objects.all()
    return render(request,"appmyweb/home.html", {"detalle": detalle})

def terminos(request):
    return render(request,"appmyweb/terminos/terminosycondiciones.html")







