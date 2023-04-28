from django.db import models

from tinymce.models import HTMLField


# Create your models here.

class TextoDetalle(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=HTMLField() 
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='TextoDetalle'
        verbose_name_plural='TextoDetalles'

    def __str__(self):
        return self.titulo