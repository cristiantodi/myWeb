from turtle import mode
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='tienda', null=True, blank=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contenido=models.CharField(max_length=1000)    
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'