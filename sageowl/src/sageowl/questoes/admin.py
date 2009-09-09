# -*- coding: utf-8 -*- 
from sageowl.questoes.models import Classificacao 
from sageowl.questoes.models import Taxionomia 
from sageowl.questoes.models import Alternativa
from sageowl.questoes.models import QuestaoDiscurssiva 
from sageowl.questoes.models import QuestaoObjetiva 

from django.contrib import admin

class AlternativaInLine(admin.TabularInline):
    model=Alternativa
    extra=5

class QuestaoAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'Referência',      {'fields': ['referencia']}),         
        (u'Questão',         {'fields': ['texto']}),
        (u'Imagem',         {'fields': ['linkImagem']}),
        (u'Som',         {'fields': ['linkSom']}),
        (u'Url',         {'fields': ['linkWeb']}),
        (u'Valor da Questão',            {'fields': ['valor']}),
        (u'Classificação da Taxionomia', {'fields': ['classificacao'], 'classes': ['collapse']}),
     ]
    inLines=[AlternativaInLine]
    list_display=('referencia','texto', 'valor', 'classificacao') 

admin.site.register(Taxionomia) 
admin.site.register(Classificacao) 
admin.site.register(QuestaoDiscurssiva, QuestaoAdmin) 
admin.site.register(QuestaoObjetiva, QuestaoAdmin) 
admin.site.register(Alternativa) 
