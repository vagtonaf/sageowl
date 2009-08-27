from django.db import models
    
class Usuario(models.Model):
    login = models.CharField(max_length = 20)
    nome = models.CharField(max_length = 100)
    password = models.CharField(max_length = 20)
    email = models.EmailField()
    perfil = models.CharField(max_length = 1) #A-Admin, U-Aluno, C-Consulta
    blk = models.BooleanField #Bloqueio de acesso
     
class Grupo(models.Model):
    nome = models.CharField(max_length = 100)
    usuarios = models.ManyToManyField(Usuario)


