# -*- coding: utf8 -*-
from django.db import models
from personas.models import *

# Create your models here.

class Inscripcion(models.Model):
    persona = models.ForeignKey(Personas)
    periodo = models.ForeignKey('Periodo', verbose_name=u'período')
    anfitrion = models.ForeignKey(Anfitrion, verbose_name=u'anfitrión')
    iglesia = models.ForeignKey(Iglesias)
    observacion = models.ForeignKey(Observacion, verbose_name=u'observación')
    def __unicode__(self):
        return u'%s (%s) en %s' %(self.persona, self.periodo, self.iglesia)
    class Meta:
        db_table = u'inscripcion'
        verbose_name_plural = 'inscripciones'
        verbose_name = u'inscripción'

class Periodo(models.Model):
    periodo = models.CharField(max_length=10,verbose_name=u'nombre')
    def __unicode__(self):
        return u'%s' %(self.periodo)
    class Meta:
        db_table = u'periodo'
        verbose_name_plural = u'períodos'
        verbose_name = u'período'

