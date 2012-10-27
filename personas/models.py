# -*- coding: utf8 -*-
from django.db import models

class Iglesias(models.Model):
    nombre = models.CharField(max_length=50,verbose_name=u'Nombre de la Iglesia')
    direccion = models.TextField(verbose_name=u'dirección')
    pastor = models.CharField(max_length=50,verbose_name='Nombre del Pastor') 
    def __unicode__(self):
        return self.nombre
    class Meta:
        db_table = u'iglesia'
        verbose_name_plural = 'iglesias'

class Anfitrion(models.Model):
    nombre = models.CharField(max_length=50,verbose_name=u'Nombre del anfitrión')
    direccion = models.TextField(verbose_name=u'dirección')
    def __unicode__(self):
        return self.nombre
    class Meta:
        db_table = u'anfitrion'
        verbose_name_plural = 'anfitriones'
        verbose_name = u'anfitrión'

class Observacion(models.Model):
    cargos = models.CharField(max_length = 20,unique=True)
    def __unicode__(self):
        return self.cargos
    class Meta:
        db_table = u'observacion'
        verbose_name_plural = 'observaciones'
        verbose_name = u'observación'

class Personas(models.Model):
    cedula = models.CharField(max_length=50,unique=True,verbose_name=u'Número de Identificación')
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=11,blank=True,verbose_name=u'teléfno')
    genero = models.IntegerField(choices=((0,'Masculino'),(1,'Femenino')),default=0,verbose_name=u'Sexo')
    iglesia = models.ForeignKey(Iglesias)
    observacion = models.ForeignKey(Observacion,verbose_name=u'observación')
    anfitrion = models.ForeignKey(Anfitrion,verbose_name=u'anfitrión')
    class Meta:
        db_table = u'personas'
        verbose_name_plural = 'personas'
    def __unicode__(self):
        return u'%s'%(self.cedula)
