# -*- coding:utf-8 -*-
from django import forms
from django.forms import ModelForm
from sageowl.questoes.models import Classificacao
   
class FormQuestao(ModelForm):
    referencia = forms.CharField()
    texto = forms.CharField()
    classificacao = forms.TypedChoiceField(Classificacao)