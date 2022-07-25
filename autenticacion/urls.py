from django.urls import path
from .views import Logear, Vregistro, cerrar_sesion
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',Vregistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),
    path('login',Logear, name="login"),
]