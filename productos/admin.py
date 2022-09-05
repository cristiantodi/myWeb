from msilib.schema import AdminExecuteSequence
from django.contrib import admin
from .models import Articulo, Categoria

# Register your models here.

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(Categoria, CategoriaAdmin)