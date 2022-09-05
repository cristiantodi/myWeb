from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name="Productos"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria")
]
