# -*- coding:utf-8 -*-
from django import forms
from django.forms import ModelForm
   
class FormQuestao(ModelForm):
    referencia = forms.CharField()
    texto = forms.CharField()
