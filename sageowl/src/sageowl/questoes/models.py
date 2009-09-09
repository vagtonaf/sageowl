# -*- coding: utf-8 -*-
from django.db import models

from django.utils.translation import ugettext as _ 
from django.conf import settings       
import datetime 
 

CHOICE_TAXIONOMIA=(
                ('Lembrar', u'Lembrança'),
                ('Entender', 'Entendimento'),
                ('Aplicar', u'Aplicação'),
                ('Analizar', 'Analize'),
                ('Avaliar', u'Avaliação'),
                ('Criar', u'Criação'),
) 
CHOICE_CLASSIFICACAO=(
                ('Reconhecer', 'Reconhecimento'),
                ('Rembrar', u'Memória'),
                ('Interpretar', u'Interpretação'),
                ('Exemplificar', u'Demostração'),
                ('Classificar', u'Classificação'),
                ('Concluir', u'Conclusão'),
                ('Comparar', u'Comparação'),
                ('Esplicar', u'Esplicação'),
                ('Resumir', u'Simplificação'),
                ('Executar', u'Execução'),
                ('Implementar', u'Implementação'),
                ('Diferenciar', u'Diferenciação'),
                ('Organizar', u'Organização'),
                ('Atribuir', u'Atribuição'),
                ('Verificar', u'Verificação'),
                ('Criticar', u'Argumentação'),
                ('Gerar', u'Geração'),
                ('Planejar', 'Planejamento'),
                ('Produzir', u'Produção'),
) 

CHOICE_LETRA=(
                ('A', 'A'),
                ('B', 'B'),
                ('C', 'C'),
                ('D', 'D'),
                ('E', 'E - Nenhuma das Alternativa'),
)

#Nova Taxionomia
#Lembrar, Entender, Aplicar, Analisar, Avaliar e Criar   
class Taxionomia(models.Model):
    nome = models.CharField(verbose_name='Nova Taxionomia', max_length = 100, choices=CHOICE_TAXIONOMIA, unique=True, default='Lembrar')
    descricao = models.TextField(verbose_name=u'Descrição',null=True)
    class Meta:
        verbose_name = u'Taxionomia'
        verbose_name_plural = u'Taxionomias'
    def __unicode__(self): 
        return self.nome 
#Classificacao
#O que o castaneda chamou de Hierarquias(Niveis)da nova taxionomia
#Lembrar (Reconhecer,Relembrar)
#Entender (Interpretar,Exemplificar,Classificar,Resumir,Concluir,Comparar,Explicar)
#Aplicar (Executar,Implementar)
#Analizar (Diferenciar,Organizar,Atribuir)
#Avaliacao (Verificar,Criticar)
#Criar (Gerar,Planejar,Produzir)

class Classificacao(models.Model):
    nome = models.CharField(verbose_name=u'Classificação da nova taxionomia', max_length = 100, choices=CHOICE_CLASSIFICACAO, unique=True)
    taxionomia = models.ForeignKey(Taxionomia)
    descricao = models.TextField(verbose_name=u'Decrição',null=True,blank=True)
    class Meta:
        unique_together = ('nome', 'taxionomia')
        verbose_name = u'Classificação'
        verbose_name_plural = u'Classificações'
    def __unicode__(self): 
        return self.nome 
    
class Questao(models.Model):
    referencia=models.CharField(max_length=20, unique=True, verbose_name=u'Referência')
    classificacao=models.ForeignKey(Classificacao, verbose_name=u'Classificação da nova taxionomia')
    texto=models.TextField()
    linkImagem=models.CharField(max_length=150,null=True,blank=True)
    linkSom=models.CharField(max_length=150,null=True,blank=True)
    linkWeb=models.CharField(max_length=50,null=True,blank=True, verbose_name='Web Site',help_text=' URL:  http://www.python.com.br')
    valor=models.FloatField(null=True,blank=True) # o valor e da questao ex 5,2
    class Meta:
        unique_together=('referencia', 'classificacao')
        verbose_name=u'Questão'
        verbose_name_plural=u'Questões'
    def __unicode__(self): 
        return self.texto
     
class QuestaoDiscurssiva(Questao):
    resposta = models.TextField()
    class Meta:
        verbose_name = u'Questão Discurssiva'
        verbose_name_plural = u'Questões Discurssivas'
    def __unicode__(self): 
        return self.resposta

class QuestaoObjetiva(Questao):
    pass
    class Meta:
        verbose_name = u'Questão Objetiva'
        verbose_name_plural = u'Questões Objetivas'
    def __unicode__(self): 
        return self.linkWebConsulta
    
class Alternativa(models.Model):
    questao = models.ForeignKey(QuestaoObjetiva, verbose_name=u'Questão Objetiva')
    letra = models.CharField(max_length = 1,default='A', choices=CHOICE_LETRA,)
    descricao = models.TextField(null=True,blank=True)
    correta = models.BooleanField(verbose_name='Correta', default=False)
    class Meta:
        unique_together = ('questao', 'letra')
        verbose_name = u'Alternativa'
        verbose_name_plural = u'Alternativas'

