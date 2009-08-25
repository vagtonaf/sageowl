from django.db import models
    
class Usuario(models.Model):
     login = models.CharField(max_length = 20)
     password = models.CharField(max_length = 20)
     email = models.EmailField()
     nome = models.CharField(max_length = 100)
     
class Grupo(models.Model):
     nome = models.CharField(max_length = 100)
     usuarios = models.ManyToManyField(Usuario)


