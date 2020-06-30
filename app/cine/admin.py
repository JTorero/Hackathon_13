from django.contrib import admin
from .models import Categoria, Pelicula, Sala, Butaca, Funcion, Ticket, Cliente

# Register your models here.

class AdminFuncion(admin.ModelAdmin):
    list_display = ("sala", "pelicula", "fecha_hora", "tarifa")
    search_fields = ("sala", "pelicula")

class AdminPelicula(admin.ModelAdmin):
    list_display = ("titulo", "duracion", "sinopsis", "reparto", "portada")
    search_fields = ("titulo", "")

class AdminButaca(admin.ModelAdmin):
    list_display = ("fila", "nom_butaca")
    search_fields = ("fila", "")

admin.site.register(Categoria)
admin.site.register(Pelicula, AdminPelicula)
admin.site.register(Sala)
admin.site.register(Butaca, AdminButaca)
admin.site.register(Funcion, AdminFuncion)
admin.site.register(Ticket)
admin.site.register(Cliente)
