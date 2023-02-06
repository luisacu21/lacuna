from django.db import models

# Create your models here.

class Pokemon (models.Model):
    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=20)
    peso = models.IntegerField()

class Entrenador(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=60)

class Gym(models.Model):
    nombre = models.CharField(max_length= 60)
    medalla = models.CharField(max_length=60)
    tipo = models.CharField (max_length=60)
