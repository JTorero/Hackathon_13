from django.forms import ModelForm, Textarea, FileInput, TextInput
from .models import Funcion, Pelicula

class CategoriaForm(ModelForm):
    class Meta:
        model = Funcion
        fields = ['sala', 'pelicula', 'fecha_hora', 'tarifa']

class PeliculaForm(ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'duracion', 'sinopsis', 'reparto', 'portada']
        labels = {
            'titulo': 'Titulo de Pelicula',
            'duracion': 'Tiempo de Duración',
            'sinopsis': 'Sinopsis',
            'reparto': 'Reparto',
            'portada': 'Imagen de Pelicula'
        }
        widgets = {
            'titulo': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Titulo de Pelicula',
                    'id': 'titulo'
                }
            ),
            'duracion': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Tiempo de Duraciónr',
                    'id': 'duracion'
                }
            ),
            'sinopsis': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Sinopsis',
                    'id': 'sinopsis'
                }
            ),
            'reparto': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Reparto',
                    'id': 'reparto'
                }
            ),
            'portada': FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'portada'
                }
            )
        }