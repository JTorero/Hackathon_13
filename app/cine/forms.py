from django.forms import ModelForm, TextInput, DateInput, EmailInput
from .models import Cliente, Funcion, Pelicula

class RegistroCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = ['dni', 'nombres', 'apellidos', 'genero', 'fecha_nacimiento', 'correo']
        labels = {
            'dni': 'Dni del cliente',
            'nombres': 'Nombre del cliente',
            'apellidos': 'Apellido del cliente',
            'fecha_nacimiento': 'Nacimiento del cliente',
            'correo': 'Correo del cliente'
        }
        widgets = {
            'dni': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese el dni',
                    'id': 'dni'
                }
            ),
            'nombres': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese el nombre',
                    'id': 'nombres'
                }
            ),'apellidos': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese el apellido',
                    'id': 'apellidos'
                }
            ),
            'genero': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Genero',
                    'id': 'genero'
                }
            ),
            'fecha_nacimiento': DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Año - mes - dia',
                    'id': 'fecha_nacimiento'
                }
            ),
            'correo': EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese el correo del autor',
                    'id': 'correo'
                }
            )
        }

class FuncionForm(ModelForm):
    class Meta:
        model = Funcion
        fields = ['sala','pelicula', 'fecha_hora', 'tarifa']

class Peliculaform(ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'duracion', 'sinopsis', 'reparto', 'portada', 'categoria']