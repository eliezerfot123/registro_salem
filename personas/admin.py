from personas.models import *
from django.contrib import admin
from lib import admin as Autocompletar

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

class AnfitrionAdmin(Autocompletar.Autocompletar):
    form=Autocompletar.make_ajax_form(Anfitrion,dict(persona='personas'))
    search_fields=['persona__nombre','persona__apellido','persona__cedula']
    list_display=('persona','direccion')
    list_filter=['persona']
admin.site.register(Anfitrion, AnfitrionAdmin)

class ObservacionAdmin(admin.ModelAdmin):
    search_fields=['cargos']
    list_filter=['cargos']
admin.site.register(Observacion, ObservacionAdmin)
