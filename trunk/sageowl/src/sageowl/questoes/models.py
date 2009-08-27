from django.db import models
#Taxionomia
#lembrar, entender, aplicar, analisar, avaliar e criar   
class Taxionomia(models.Model):
    nome = models.CharField(max_length = 100, unique=True)
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
    nome = models.CharField(max_length = 100, unique=True)
    taxionomia = models.ForeignKey(Taxionomia)
    descricao = models.TextField()
    class Meta:
        unique_together = ('nome', 'taxionomia')
        verbose_name = u'Classificacao'
        verbose_name_plural = u'Classificacoes'
    def __unicode__(self): 
        return self.nome 
    
class Questao(models.Model):
    nome = models.CharField(max_length = 100)
    classificacao = models.ForeignKey(Classificacao)
    valor = models.FloatField(null=True) # o valor e da questao ex 5,2
    class Meta:
        unique_together = ('nome', 'classificacao')
        verbose_name = u'Questao'
        verbose_name_plural = u'Questoes'
    def __unicode__(self): 
        return self.nome 

     
class QuestaoDiscurssiva(Questao):
    resposta = models.TextField()

class QuestaoObjetiva(Questao):
    pass
    
class Alternativa(models.Model):
    questao = models.ForeignKey(QuestaoObjetiva)
    letra = models.CharField(max_length = 1)
    descricao = models.TextField()
    correta = models.BooleanField()
    class Meta:
        unique_together = ('questao', 'letra')
        unique_together = ('questao', 'correta')
        verbose_name = u'Alternativa'
        verbose_name_plural = u'Alternativas'

