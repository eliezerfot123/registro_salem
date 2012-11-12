# -*- coding: utf8
from personas.models import *
from django.db.models import Q

'''Autocompletado para Estudiantes'''
class PersonasLookup(Personas):
    def get_query(self,q,request):
        return Personas.objects.filter(cedula__istartswith=q)

    def format_result(self,personas):
        return u'%s - %s %s' % (personas.cedula, personas.nombre, personas.apellido)

    def format_item(self,Personas):
        return unicode(Personas)

    def get_objects(self,ids):
        return Personas.objects.filter(pk__in=ids).order_by('persona__cedula','persona__nombre','primer_apellido')
