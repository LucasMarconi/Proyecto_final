from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    
    def __str__ (self):
        return f"{self.nombre} - {self.precio}"

class Sucursal(models.Model):
    calle = models.CharField(max_length=40)
    altura = models.IntegerField()
    
    def __str__ (self):
        return f"{self.calle} - {self.altura}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    edad = models.IntegerField()
    
    def __str__ (self):
        return f"{self.nombre} - {self.email}"