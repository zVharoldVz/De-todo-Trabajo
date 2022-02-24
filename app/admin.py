from django.contrib import admin
from .models import *
# Register your models here.

class TipoTrabajoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipotrabajo')

class AlbumImageInline(admin.TabularInline):
    model = Foto_perfil
    extra = 3

class AlbumAdmin(admin.ModelAdmin):
    inlines = [ AlbumImageInline, ]

admin.site.register(TipoTrabajo,TipoTrabajoAdmin)
admin.site.register(Habilidades)
admin.site.register(Foto_perfil)