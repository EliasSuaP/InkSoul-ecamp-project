from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'
    

# Clases para los tatuadores
class Tatuadores(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    descripcion = models.TextField()

    def __str__(self) -> str:
        return f'{self.nombre}'
    

# CLases para las galerías
class Animale(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=200) # URLField era

    def __str__(self) -> str:
        return f'{self.nombre}'


class Maorie(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.nombre}'

class Mitologico(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.nombre}'


class Reserva(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

# Clase para productos/kits
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    url = models.URLField()

    def __str__(self) -> str:
        return f'{self.nombre}'
