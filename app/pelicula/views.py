from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Pelicula
from .forms import PeliculaForm
from django.urls import reverse_lazy

# Create your views here.
class Home(TemplateView):
    template_name = 'pelicula/index.html'

class ListPeliculas(ListView):
    model = Pelicula
    template_name = 'pelicula/peliculas/list_pelicula.html'
    queryset = Pelicula.objects.all()
    context_object_name = 'peliculas'

class CreatePelicula(CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'pelicula/peliculas/create_pelicula.html'
    success_url = reverse_lazy('pelicula:list.peliculas')

class UpdatePelicula(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'pelicula/peliculas/update_pelicula.html'
    success_url = reverse_lazy('pelicula:list.peliculas')

class DeletePelicula(DeleteView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'pelicula/peliculas/delete.html'
    success_url = reverse_lazy('pelicula:list.peliculas')
    
    def get_context_data(self, **kwargs):   
        pelicula = Pelicula.objects.get(id=self.kwargs.get('pk'))
        context = super(DeletePelicula, self).get_context_data(**kwargs)
        context['peliculas'] = pelicula
        return context