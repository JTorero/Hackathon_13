from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import Home, ListPeliculas, CreatePelicula, UpdatePelicula, DeletePelicula

urlpatterns = [
    path('', login_required(Home.as_view()), name='index'),
    path('list_pelicula', login_required(ListPeliculas.as_view()), name='list.peliculas'),
    path('create_pelicula', login_required(CreatePelicula.as_view()), name='create.peliculas'),
    path('update_pelicula/<int:pk>', login_required(UpdatePelicula.as_view()), name='update.peliculas'),
    path('delete_pelicula/<int:pk>', login_required(DeletePelicula.as_view()), name='delete.peliculas')
]