from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Servicios(models.Model):
    servicio = models.CharField(max_length=40)
    descripcion = models.TextField()

    def __str__(self):
        return self.servicio


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=75)
    ubicacion = models.CharField(max_length=150)
    mercado = models.CharField(max_length=50)
    telefono = PhoneNumberField(max_length=12)

    def __str__(self):
        return self.usuario


class Cotizaciones(models.Model):
    titulo = models.CharField(max_length=20)
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    descripcion = models.TextField()
    status = models.IntegerField()

    def __str__(self):
        return self.titulo

    class Meta:
        permissions = [
            ('administracion', 'administracion de cotizaciones')
        ]


class Tareas(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_finalizacion = models.DateTimeField()
    administrador_creador = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='creador')
    administrador_encargado = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='encargado')

    def __str__(self):
        return self.titulo
