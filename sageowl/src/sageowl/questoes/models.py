from django.db import models
 
class Classificacao(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    valor = models.CharField(max_length=20)
   
class Questao(models.Model):
    nome = models.CharField(max_length = 100)
    classificacao = models.ForeignKey(Classificacao)
    #class Meta:
    #    abstract = True
     
class QuestaoDiscurssiva(Questao):
    resposta = models.TextField()

class QuestaoObjetiva(Questao):
    pass

class Alternativa(models.Model):
    questao = models.ForeignKey(QuestaoObjetiva)
    descricao = models.TextField()
    correta = models.BooleanField()

