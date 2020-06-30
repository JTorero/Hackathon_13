from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import Home, RegistroCliente, ListFuncion, ListPeliculas

urlpatterns = [
    path('', Home.as_view(), name="index"),
    path('list_funcion/<int:pk>', ListFuncion.as_view(), name="list.funcion"),
    path('list_pelicula', ListPeliculas.as_view(), name="list.pelicula"),
    path('registro_cliente', RegistroCliente.as_view(), name="registro.cliente")
]