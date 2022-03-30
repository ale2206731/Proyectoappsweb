from re import search
from django.contrib import admin
from .models import Comentario, Noticias

# Register your models here.
class NotiAdmin(admin.ModelAdmin):
    list_display = ["encabezado", "descripcion", "autor", "fecha"]
    list_editable =["autor"]
    search_fields = ["encabezado", "descripcion", "autor"]
    list_filter = ["fecha"]
    list_per_page = 10


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ["nombre", "email", "telefono", "comentario"]
    list_editable = ["comentario"]
    search_fields = ["email"]
    list_per_page = 10



    

    # Register your models here.
admin.site.register(Noticias,NotiAdmin)
admin.site.register(Comentario, ComentarioAdmin)
   