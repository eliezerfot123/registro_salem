from personas.models import *
from django.contrib import admin

class PersonasAdmin(admin.ModelAdmin):
    search_fields=['cedula']
    list_display=('cedula','nombre','apellido')
    list_filter = ['cedula']
admin.site.register(Personas, PersonasAdmin)

class IglesiasAdmin(admin.ModelAdmin):
    search_fields=['nombre']
    list_display=('nombre','pastor')
    list_filter=['nombre']
admin.site.register(Iglesias, IglesiasAdmin)

class AnfitrionAdmin(admin.ModelAdmin):
    search_fields=['nombre']
    list_display=('nombre','direccion')
    list_filter=['nombre']
admin.site.register(Anfitrion, AnfitrionAdmin)

class ObservacionAdmin(admin.ModelAdmin):
    search_fields=['cargos']
    list_filter=['cargos']
admin.site.register(Observacion, ObservacionAdmin)
