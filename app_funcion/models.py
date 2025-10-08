from django.db import models

# Create your models here.
#Clase Funciones con los campos NombrePelicula, FechaHora y Idioma
class Funcion(models.Model):
    nombrePelicula = models.CharField(max_length=255)
    Fecha_Hora = models.DateTimeField()
    Idioma = models.CharField(max_length=50)

    def __str__(self):
        return self.nombrePelicula