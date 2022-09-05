from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    #contenido=HTMLField()
    contenido=models.CharField(max_length=500)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'

    def __str__(self):
        return self.titulo