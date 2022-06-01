from django.urls import path
from appmyweb import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('tienda', views.tienda, name="Tienda"),
    path('servicios', views.servicios, name="Servicios"),
    path('contacto', views.contacto, name="Contacto"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)