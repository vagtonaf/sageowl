from django.db import models

from django.utils.translation import ugettext as _ 
from django.conf import settings       
import datetime 
 

CHOICE_TAXIONOMIA=(
                ('Lembrar', 'Lembranca'),
                ('Entender', 'Entendimento'),
                ('Aplicar', 'Aplicacao'),
                ('Analizar', 'Analize'),
                ('Avaliar', 'Avaliacao'),
                ('Criar', 'Criacao'),
) 
CHOICE_CLASSIFICACAO=(
                ('Reconhecer', 'Reconhecimento'),
                ('Rembrar', 'Memoria'),
                ('Interpretar', 'Interprementacao'),
                ('Exemplificar', 'Demostracao'),
                ('Classificar', 'Classificacao'),
                ('Concluir', 'Conclusao'),
                ('Comparar', 'Comparacao'),
                ('Esplicar', 'Esplicacao'),
                ('Resumir', 'Simplificao'),
                ('Executar', 'Execucao'),
                ('Implementar', 'Implementacao'),
                ('Diferenciar', 'Diferenciacao'),
                ('Organizar', 'Organizacao'),
                ('Atribuir', 'Atribuicao'),
                ('Verificar', 'Verificacao'),
                ('Criticar', 'Argumentacao'),
                ('Gerar', 'Geracao'),
                ('Planejar', 'Planejamento'),
                ('Produzir', 'Producao'),
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
    nome = models.CharField(verbose_name="Nova Taxionomia", max_length = 100, choices=CHOICE_TAXIONOMIA, unique=True, default='Lembrar')
    descricao = models.TextField()
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
    nome = models.CharField(verbose_name="Classificacao da nova taxionomia", max_length = 100, choices=CHOICE_CLASSIFICACAO, unique=True)
    taxionomia = models.ForeignKey(Taxionomia)
    descricao = models.TextField()
    class Meta:
        unique_together = ('nome', 'taxionomia')
        verbose_name = u'Classificacao'
        verbose_name_plural = u'Classificacoes'
    def __unicode__(self): 
        return self.nome 
    
class Questao(models.Model):
    referencia = models.CharField(max_length = 20, unique=True)
    classificacao = models.ForeignKey(Classificacao, verbose_name="Classificacao da nova taxionomia")
    texto = models.TextField()
    linkImagem=models.CharField(max_length = 150)
    linkSom=models.CharField(max_length = 150)
    valor = models.FloatField(null=True) # o valor e da questao ex 5,2
    class Meta:
        unique_together = ('referencia', 'classificacao')
        verbose_name = u'Questao'
        verbose_name_plural = u'Questoes'
    def __unicode__(self): 
        return self.texto 
     
class QuestaoDiscurssiva(Questao):
    resposta = models.TextField()

class QuestaoObjetiva(Questao):
    linkWebConsulta = models.CharField(max_length=50, verbose_name='Website', 
help_text=' URL:  http://www.exemplo.com.br')
#    pass
    
class Alternativa(models.Model):
    questao = models.ForeignKey(QuestaoObjetiva)
    letra = models.CharField(max_length = 1,default='A', choices=CHOICE_LETRA,)
    descricao = models.TextField()
    correta = models.BooleanField(verbose_name="Correta", default=False)
    class Meta:
        unique_together = ('questao', 'letra')
        verbose_name = u'Alternativa'
        verbose_name_plural = u'Alternativas'

