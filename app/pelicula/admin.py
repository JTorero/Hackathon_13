from django.contrib import admin
from .models import Categoria, Pelicula, Sala, Butaca, Funcion, Ticket, Cliente

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Pelicula)
admin.site.register(Sala)
admin.site.register(Butaca)
admin.site.register(Funcion)
admin.site.register(Ticket)
admin.site.register(Cliente)
