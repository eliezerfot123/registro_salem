# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from personas.models import *
from ajax_select.fields import AutoCompleteSelectField

#Para el perfil del estudiante

class AnfitrionForm(forms.ModelForm):
    persona = AutoCompleteSelectField('personas')
    class Meta:
        model = Personas

