# -*- coding:utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.localflavor.br.forms import BRZipCodeField
from django.contrib.localflavor.br.forms import BRPhoneNumberField
from django.contrib.localflavor.br.forms import BRCPFField
from django.contrib.localflavor.br.forms import BRStateChoiceField
from sageowl.pessoas.models import Avaliado

class AvaliadoForm(ModelForm):
    referencia = forms.CharField()
    cep = BRZipCodeField(label='CEP')
    turma = forms.CharField()
    estado = BRStateChoiceField(label='Estado')
    cpf = BRCPFField(label='CPF', required=False)
    foneresidencial = BRPhoneNumberField(label='Telefone')

    class Meta:
        model = Avaliado