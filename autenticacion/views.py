from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.

class Vregistro(View):
    def get (self,request):
        form = UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})
        pass

    def post(self, request):
        form=UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario=form.save()
            login(request, usuario) #Para realizar login
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request,"registro/registro.html",{"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect('Tienda')

def Logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombreUsuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombreUsuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Tienda')
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Informacion incorrecta")
    
    form = AuthenticationForm()
    return render(request, "login/login.html", {"form":form})
