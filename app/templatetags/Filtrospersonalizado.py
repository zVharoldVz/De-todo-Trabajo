from django import template
from django.db.models import Avg
from app.models import *

register = template.Library()

@register.filter(name='existing_Fototrabajo')
def existing_Fototrabajo(id):
    return FotoTrabajo.objects.filter(habilidad_id = id)

@register.filter(name='existing_FotoValoracion')
def existing_FotoValoracion(id):
    return FotoValoracion.objects.filter(clasifiacion_id = id)

@register.simple_tag
def existing_FotoValoracion_exist(id):
    return FotoValoracion.objects.filter(clasifiacion_id = id).exists()

@register.simple_tag
def Pedido_Solicitados(value,id):
    return value.exclude(user_id = id)

@register.simple_tag
def Pedido_Realizado(value,id):
    return value.filter(user_id = id)

@register.simple_tag
def starHabilidad(value):
    Dato = Clasifiacion.objects.filter(habilidad_id=value).aggregate(Avg('puntuacion'))['puntuacion__avg']
    if (Dato is None):
        Dato=0
    return Dato

@register.simple_tag
def starHabilidadporcentaje(value):
    return (100*value)/5

@register.simple_tag
def staruser(value):
    return Clasifiacion.objects.filter(habilidad__user__id=value).aggregate(Avg('puntuacion'))['puntuacion__avg']

@register.simple_tag
def ComentariosHabilidad(value):
    Dato = Clasifiacion.objects.filter(habilidad_id=value).aggregate(Avg('puntuacion'))['puntuacion__avg']
    if (Dato is None):
        Dato=0
    return Dato



@register.simple_tag
def get_active(n):
    Dato = ""
    if n==0:
        Dato ="active"
    return Dato

@register.simple_tag
def get_colum(Value,Defaut,Cambio,donde):
    Dato = Defaut
    if Value==donde:
        Dato = Cambio
    return Dato

@register.simple_tag
def get_Color_estado(n):
    Dato = ""
    if n=='Pendiente':  Dato = "bg-primary"
    elif n=='Aceptado': Dato = "bg-success"
    elif  n=='Cancelado': Dato = "bg-danger"
    else:  Dato = "bg-secondary"
    return Dato

