# -*- coding:utf-8 -*-
from django import forms
from sageowl.questoes.models import Classificacao
   
class FormQuestao(forms.Form):
    referencia = forms.CharField()
    texto = forms.CharField()
    # classificacao = forms.TypedChoiceField(Classificacao) 