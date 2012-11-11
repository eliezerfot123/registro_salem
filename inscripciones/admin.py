# -*- coding: utf8 -*-
from django.contrib import admin
from inscripciones.models import *
from lib import admin as Autocompletar

class InscripcionesAdmin(Autocompletar.Autocompletar):
    form=Autocompletar.make_ajax_form(Inscripcion,dict(persona='personas'))
    search_fields=['persona__cedula', 'persona__nombre', 'persona__apellido']
    list_filter=['periodo']
admin.site.register(Inscripcion, InscripcionesAdmin)

class PeriodoAdmin(admin.ModelAdmin):
    search_fields=['periodo__periodo']
admin.site.register(Periodo, PeriodoAdmin)
