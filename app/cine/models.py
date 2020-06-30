from django.db import models
#blank=True para campos de tipo Texto y null=True para campos tipo Fecha o Numerico

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nombre_categoria

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    duracion = models.PositiveIntegerField(blank=False, null=False)
    sinopsis = models.TextField(blank=False, null=False)
    reparto = models.CharField(max_length=150, blank=True, null=True)
    portada = models.ImageField(upload_to='pictures/pelicula', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_sala = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre_sala

class Funcion(models.Model):
    id = models.AutoField(primary_key=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now=False, auto_now_add=False, blank = False, null = False)
    tarifa = models.FloatField()

    def __str__(self):
        return self.pelicula.titulo + 'Hora:' + str(self.fecha_hora) + str(self.tarifa)

class Butaca(models.Model):
    id = models.AutoField(primary_key=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    fila = models.PositiveIntegerField(blank=False,null=False)
    nom_butaca = models.CharField(max_length=1, blank=False,null=False)

    def __str__(self):
        return self.sala.nombre_sala + str(self.fila) + self.nom_butaca

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.IntegerField()
    nombres = models.CharField(max_length=100, blank=False, null=False)
    apellidos = models.CharField(max_length=100, blank=False, null=False)
    genero = models.CharField(max_length=1)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombres + '-' + str(self.dni)

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    butacas = models.ManyToManyField(Butaca)