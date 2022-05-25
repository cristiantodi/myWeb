from django.urls import path
from appmyweb import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('tienda', views.tienda, name="Tienda"),
    path('servicios', views.servicios, name="Servicios"),
    path('contacto', views.contacto, name="Contacto"),
]