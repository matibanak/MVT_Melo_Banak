from ssl import Options
from django.db import models


# Create your models here.

class Familiares(models.Model):
    nombre= models.CharField(max_length=40) #campo de texto
    apellido= models.CharField(max_length=40) #campo de enteros
    fecha_nacimiento= models.CharField(max_length=40)
    anios=models.IntegerField()

    def __str__(self):
        return self.nombre+"  "+str(self.apellido)+"  "+str(self.anios)

class Negocios(models.Model):
    nombre1= models.CharField(max_length=40)
    provincia= models.CharField(max_length=40)
    pais= models.CharField(max_length=40)
    telefono= models.IntegerField()

    def __str__(self):
        return self.nombre1+"  "+str(self.provincia)+"  "+str(self.telefono)

class Inmobiliarios(models.Model):
    direccion= models.CharField(max_length=60)
    localidad= models.CharField(max_length=40)
    mt2= models.IntegerField()

    def __str__(self):
        return self.direccion+"  "+str(self.localidad)+"  "+str(self.mt2)



