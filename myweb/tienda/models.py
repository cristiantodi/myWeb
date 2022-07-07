from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    imagen_categoria=models.ImageField(upload_to='categoria', null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='tienda', null=True, blank=True)
    categorias=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    contenido=models.CharField(max_length=1000)    
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre