from django.db import models

#O que o castaneda chamou de Hierarquias(Niveis)da nova taxionomia
#Lembrar (Reconhecer,Relembrar)
#Entender (Interpretar,Exemplificar,Classificar,Resumir,Concluir,Comparar,Explicar)
#Aplicar (Executar,Implementar)
#Analizar (Diferenciar,Organizar,Atribuir)
#Avaliacao (Verificar,Criticar)
#Criar (Gerar,Planejar,Produzir)

class Nivel(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()

#lembrar, entender, aplicar, analisar, avaliar e criar   
class Classificacao(models.Model):
    nome = models.CharField(max_length = 100)
    nivel = models.ForeignKey(Nivel)
    descricao = models.TextField()
    
class Questao(models.Model):
    nome = models.CharField(max_length = 100)
    classificacao = models.ForeignKey(Classificacao)
    valor = models.CharField(max_length=20) # o valor é da questao
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

