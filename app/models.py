import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MaxValueValidator
from django.db.models import signals
from django.dispatch import receiver 
# Create your models here.

"""
When a User is saved, send the post_save signal. When a User is saved and the signal was sent by the
creation of the User instance, then execute the code in the body of the function
:param sender: The model class
:param instance: The object that was just created
:param created: a boolean; True if a new record was created, False if an existing record was updated
"""
@receiver(signals.post_save, sender=User) 
def create_user(sender, instance, created, **kwargs):
    if created:
        ExtraDato.objects.create(telefono="", dni="", Direcion="",user_id=instance.id)
        Foto_perfil.objects.create(imagen="",user_id=instance.id)


# ExtraDato is a model that extends the User model
class ExtraDato(models.Model):
    telefono = models.CharField(max_length=10)
    dni = models.CharField(max_length=8)
    Direcion = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.dni
        
# This class is used to store the profile picture of the user
class Foto_perfil(models.Model):
    imagen = models.ImageField(upload_to='DeTodoTrabajo/FotoUser/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.username

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nombrehabilidad

# A FotoTrabajo is a file uploaded by a user to a Habilidades
class FotoTrabajo(models.Model):
    fotoTrabajo = models.ImageField(upload_to='DeTodoTrabajo/FotoTrabajo/')
    habilidad = models.ForeignKey(Habilidades, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.fotoTrabajo


# Clasificacion is a model that has a comentario, puntuacion, and user
class Clasifiacion(models.Model):
    comentario = models.CharField(max_length=1000)
    puntuacion = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.comentario


# FotoValoracion is a model that has a fotoValoracion and clasifiacion
class FotoValoracion(models.Model):
    fotoValoracion = models.ImageField(upload_to='DeTodoTrabajo/fotoValoracion/')
    clasifiacion = models.ForeignKey(Clasifiacion, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.fotoValoracion

