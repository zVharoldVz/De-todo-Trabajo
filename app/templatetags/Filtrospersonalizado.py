from django import template

from app.models import *

register = template.Library()

@register.filter(name='existing_Fototrabajo')
def existing_Fototrabajo(id):
    return FotoTrabajo.objects.filter(habilidad_id = id)


@register.simple_tag
def Pedido_Solicitados(value,id):
    return value.exclude(user_id = id)

@register.simple_tag
def Pedido_Realizado(value,id):
    return value.filter(user_id = id)


@register.simple_tag
def get_active(n):
    Dato = ""
    if n==0:
        Dato ="active"
    return Dato

