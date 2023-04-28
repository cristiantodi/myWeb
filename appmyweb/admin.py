from django.contrib import admin
from .models import TextoDetalle

# Register your models here.

class TextoAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')

admin.site.register(TextoDetalle, TextoAdmin)