from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Pelicula, Cliente
from .forms import RegistroCliente
from django.urls import reverse_lazy

# Create your views here.
class Home(TemplateView):
    template_name = 'cine/index.html'

class ListPelicula(ListView):
    model = Pelicula
    template_name = 'cine/pelicula/list_pelicula.html'
    queryset = Pelicula.objects.all()
    context_object_name = 'peliculas'

class RegistroCliente(CreateView):
    model = Cliente
    form_class = RegistroCliente
    template_name = 'cine/cliente/registro_cliente.html'
    success_url = reverse_lazy('cine:list.pelicula')