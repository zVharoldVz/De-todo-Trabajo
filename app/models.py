import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MaxValueValidator
from django.db.models import signals
from django.dispatch import receiver 
from django.contrib.auth.models import AbstractUser
# Create your models here.


#@receiver(signals.post_save, sender=User) 
#def create_user(sender, instance, created, **kwargs):
#    if created:


class User(AbstractUser):
    telefono = models.CharField('Télefono', max_length=15)
    dni = models.CharField(max_length=8)
    Direcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='DeTodoTrabajo/FotoUser/',default='DeTodoTrabajo/Defaut/User-Login.png')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'dni',]

# A tipo trabajo is a type of work
class TipoTrabajo(models.Model):
    tipotrabajo = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.tipotrabajo

# Habilidades is a model that has a name, a description and a type of work
class Habilidades(models.Model):
    nombrehabilidad = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000,default='Sin Descripcion')
    nomeroTrabjos = models.IntegerField(default=0)
    tipoTrabajo = models.ForeignKey(TipoTrabajo, on_delete=models.CASCADE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nombrehabilidad

# A FotoTrabajo is a file uploaded by a user to a Habilidades
class FotoTrabajo(models.Model):
    fotoTrabajo = models.ImageField(upload_to='DeTodoTrabajo/FotoTrabajo/')
    habilidad = models.ForeignKey(Habilidades, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.fotoTrabajo

    def delete(self, *args, **kwargs):
        self.document.delete()
        return super().delete(*args, **kwargs)

# Clasificacion is a model that has a comentario, puntuacion, and user
class Clasifiacion(models.Model):
    comentario = models.CharField(max_length=1000)
    puntuacion = models.FloatField()
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    habilidad = models.ForeignKey(Habilidades, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.comentario


# FotoValoracion is a model that has a fotoValoracion and clasifiacion
class FotoValoracion(models.Model):
    fotoValoracion = models.ImageField(upload_to='DeTodoTrabajo/fotoValoracion/')
    clasifiacion = models.ForeignKey(Clasifiacion, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.fotoValoracion

class Pedido(models.Model):
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=20)
    habilidad = models.ForeignKey(Habilidades, on_delete=models.CASCADE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.username

class Favoritos(models.Model):
    fecha= models.DateTimeField()
    habilidad = models.ForeignKey(Habilidades, on_delete=models.CASCADE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.username