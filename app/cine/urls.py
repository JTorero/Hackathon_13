from django.urls import path
from .views import Home, ListPelicula, RegistroCliente

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('registro_cliente', RegistroCliente.as_view(), name='registro.cliente' ),
    path('list_pelicula', ListPelicula.as_view(), name='list.pelicula')
]