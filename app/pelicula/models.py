from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    categoria = models.CharField(max_length = 50, blank = False, null = False)

    def __str__(self):
        return self.categoria

class Pelicula(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 200, blank = False, null = False)
    duracion = models.IntegerField(blank = False, null = False)
    sinopsis = models.TextField(blank = False, null = False)
    reparto = models. CharField(max_length = 500, blank = True, null = True)
    portada = models.ImageField(upload_to = 'pictures/pelicula', blank = True, null = True)
    categoria = models.ForeignKey('Categoria',on_delete = models.CASCADE )
    def __str__(self):
        return self.titulo

class Sala(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_sala = models.CharField(max_length = 10, blank = False, null = False)
    def __str__(self):
        return self.nombre_sala

class Butaca(models.Model):
    id = models.AutoField(primary_key = True)
    sala =  models.ForeignKey('Sala', on_delete = models.CASCADE)
    fila = models.CharField(max_length = 2, blank = False, null = False)
    num_butaca = models.IntegerField(blank = False, null = False)
    def __str__(self):
        return self.fila + '-'+ str(self.num_butaca)

class Funcion(models.Model):
    id = models.AutoField(primary_key = True)
    sala = models.ForeignKey('Sala', on_delete = models.CASCADE)
    pelicula = models.ForeignKey('Pelicula', on_delete = models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now=False, auto_now_add=False, blank = False, null = False)
    tarifa = models.IntegerField( blank = False, null = False)

    def __str__(self):
        return self.Pelicula.titulo + ' Hora: ' + str(self.fecha_hora)

class Cliente(models.Model):
    id = models.AutoField(primary_key = True)
    dni = models.IntegerField()
    nombres= models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 50)
    genero = models.CharField(max_length = 1)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField()
    def __str__(self):
        return self.dni + ' - ' + self.nombres
class Ticket(models.Model):
    id = models.AutoField(primary_key = True)
    funcion = models.ForeignKey('Funcion', on_delete = models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete = models.CASCADE)
    butacas = models.ManyToManyField(Butaca)



