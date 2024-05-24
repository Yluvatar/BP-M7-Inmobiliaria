from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

tipos_usuario = (
    ('arrendatario', 'Arrendatario'),
    ('arrendador', 'Arrendador'),
)

class Region(models.Model):
    nombre = models.CharField(max_length=100, default='', blank=False, null=False)
    numero = models.IntegerField(default=0, blank=False, null=False)
    romano = models.CharField(max_length=5, default='', blank=False, null=False)


class Provincia(models.Model):
    nombre = models.CharField(max_length=50, default='', blank=False, null=False)
    region_id = models.ForeignKey(Region, on_delete=models.PROTECT)


class Comuna(models.Model):
    nombre = models.CharField(max_length=50, default='', blank=False, null=False)
    provincia_id = models.ForeignKey(Provincia, on_delete=models.PROTECT)


class tipo_propiedad(models.Model):
    nombre = models.CharField(max_length=50, default='', blank=False, null=False)


class Usuario(AbstractUser):
    rut = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    tipo_usuario = models.CharField(max_length=15, choices=tipos_usuario, default='arrendatario')


class Propiedad(models.Model):
    nombre = models.CharField(max_length=150, default='', blank=False, null=False)
    descripcion = models.TextField(max_length=500, default='', blank=False, null=False)
    m2_construidos = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=False, null=False)
    m2_terreno = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=False, null=False)
    estacionamientos = models.IntegerField(default=0, blank=False, null=False)
    habitaciones = models.IntegerField(default=1, blank=False, null=False)
    banios = models.IntegerField(default=1, blank=False, null=False)
    direccion = models.CharField(max_length=150, default='', blank=False, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=False, null=False)
    uf = models.BooleanField(default=False, blank=False, null=False)
    tipo_propiedad_id = models.ForeignKey(tipo_propiedad, on_delete=models.PROTECT)
    comuna_id = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
