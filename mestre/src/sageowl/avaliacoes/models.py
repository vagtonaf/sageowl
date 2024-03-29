# -*- coding: utf-8 -*-
from django.db import models
from sageowl.questoes.models import Questao
from sageowl.pessoas.models import Avaliador
from sageowl.pessoas.models import Avaliado
from sageowl.instituicoes.models import Turma

from django.utils.translation import ugettext as _ 
from django.conf import settings       
import datetime 

CHOICE_TIPO_AVALIACAO=(
    ('P'      ,  'Prova'  ),
    ('T'      ,  'Teste'  ),
    ('S'      ,  'Simulado'  ),
) 
CHOICE_TIPO_PROVA=(
    ('P1'      ,  'P1'  ),
    ('P2'      ,  'P2'  ),
    ('P3'      ,  'P3'  ),
    ('PF'      ,  'PF'  ),
    ('2CHP1'      ,  '2 Chamada P1' ),
    ('2CHP2'      ,  '2 Chamada P2' ),
    ('2CHP3'      ,  '2 Chamada P3' ),
    ('2CHPF'      ,  '2 Chamada PF' ),
    ('RP'      ,  u'Recuperação' ),
) 
class Avaliacao(models.Model):
    referencia=models.CharField(max_length=20, unique=True, verbose_name=u'Referência')
    turma=models.ForeignKey(Turma)
    dt_avaliacao=models.DateTimeField(verbose_name=u'Data da Avaliação',null=True,blank=True)
    tipoAvaliacao = models.CharField(u'Tipo de Avaliação',max_length=1,choices=CHOICE_TIPO_AVALIACAO,null=True)
    class Meta:
        verbose_name=u'Avaliação'
        verbose_name_plural=u'Avaliações'
    def __unicode__(self): 
        return self.referencia    

class Prova(models.Model):
    avaliacao=models.ForeignKey(Avaliacao)
    questao=models.ForeignKey(Questao, verbose_name=u'Questão')
    tipoProva = models.CharField('Tipo de Prova',max_length=10,choices=CHOICE_TIPO_PROVA,null=True,blank=True)    
    class Meta:
        verbose_name=u'prova'
        verbose_name_plural=u'Provas'
    def __unicode__(self): 
        return self.resposta 

class Resolucao(models.Model):
    avaliador=models.ForeignKey(Avaliador)
    avaliado=models.ForeignKey(Avaliado)
    prova=models.ForeignKey(Prova)
    resposta=models.TextField(verbose_name='Resposta do Avaliado',null=True,blank=True) #Resposta da discursiva
    obsAvaliador=models.TextField(verbose_name=u'Observação do Avaliador',null=True,blank=True)
    respostaAvaliador=models.BooleanField(verbose_name='Correta', default=False,null=True,blank=True) # o avaliador  resposnde se esta correta
    notaAvaliador=models.FloatField(verbose_name='Nota do Avaliador', null=True,blank=True) # o nota dada pelo avaliador da questao ex 5,2
    dth_resolucao=models.DateTimeField(verbose_name=u'Data de Resolução', auto_now_add=True)
    dth_correcao=models.DateTimeField(verbose_name=u'Data de Correção',null=True,blank=True)
    class Meta:
        verbose_name=u'Resolução'
        verbose_name_plural=u'Resoluções'
    def __unicode__(self): 
        return self.resposta 
    





