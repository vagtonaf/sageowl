from django.db import models
    
class Usuario(models.Model):
    login = models.CharField(max_length = 20, unique=True)
    nome = models.CharField(max_length = 100)
    password = models.CharField(max_length = 20)
    email = models.EmailField()
    perfil = models.CharField(max_length = 1, blank=True, null=True) #A-Admin, U-Aluno, C-Consulta
    blk = models.BooleanField(verbose_name="Ativo", default=True) #Bloqueio de acesso
     
class Grupo(models.Model):
    nome = models.CharField(max_length = 100, unique=True)
    usuarios = models.ManyToManyField(Usuario)


