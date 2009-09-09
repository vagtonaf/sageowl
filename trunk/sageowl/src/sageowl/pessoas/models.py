# -*- coding: utf-8 -*-
from sageowl.instituicoes.models import Turma
from django.db import models
from django.utils.translation import ugettext as _ 
from django.conf import settings       
import datetime 

CHOICE_SEXO=(
    ('M'    ,  'Masculino'),
    ('F'      ,  'Feminino'  ),
)

CHOICE_ESTADO=(
    ('MG'      ,  'Minas Gerais'  ),
    ('BA',u'Bahía'),
    ('PB',u'Paraíba'),
    ('AL','Alagoas'),
    ('GO','Goias'),
    ('MT','Mato Grosso'),
    ('MG','Minas Gerais'),
    ('PE','Pernambuco'),
    ('RO',u'Rondônia'),
    ('RR','Rorãima'),
    ('SC','Santa Catarina'),
    ('SP','Sao Paulo'),
    ('SE','Sergipe'),
    ('TO','Tocantins'),
    ('AC','Acre'),
    ('AP',u'Amapá'),
    ('AM','Amazonas'),
    ('CE',u'Ceará'),
    ('ES','Espirito Santo'),
    ('MA',u'Maranhão'),
    ('MS','Mato Grosso do Sul'),
    ('PA',u'Pará'),
    ('PR','Parana'),
    ('PI',u'Piauí'),
    ('RJ','Rio de Janeiro'),
    ('RN','Rio Grande do Norte'),
    ('RS','Rio Grande do Sul'),
)

CHOICE_CIVIL=(
    ('C'      ,  'Casado'  ),
    ('S'    ,  'Solteiro'),
    ('D'      ,  'Divorciado'  ),
)

CHOICE_SIM_NAO=(
    ('S'      ,  'Sim'  ),
    ('N'      ,  'Nao'  ),
) 

CHOICE_PERFIL=(
    ('A'      ,  'Administrador'  ),
    ('U'      ,  'Usuario'  ),
    ('C'      ,  'Usuario de Consulta'  ),
) 

class Pessoa(models.Model): 
    nome = models.CharField('Nome',max_length=100) 
    mae = models.CharField(u'Nome da Mãe',max_length=100,null=True,blank=True) 
    pai = models.CharField('Nome do Pai',max_length=100,null=True,blank=True) 
    dt_nasc = models.DateField('Data de Nascimento',null=True,blank=True) 
    naturalidade = models.CharField('Naturalicade',max_length=100,null=True,blank=True) 
    nacionalidade = models.CharField('Nacionalidade',max_length=100,null=True,blank=True)
    sexo = models.CharField('Sexo',max_length=1,default='M',choices=CHOICE_SEXO) 
    rg = models.CharField('RG',max_length=25,null=True,blank=True) 
    rgorgexp = models.CharField('Orgao Expedidor',max_length=15,null=True,blank=True) 
    uf = models.CharField('UF',max_length=2,default='RJ',choices=CHOICE_ESTADO,null=True,blank=True) 
    cpf = models.CharField('CPF',max_length=11,null=True,blank=True) 
    estadocivil = models.CharField('Estado Civil',max_length=1,choices=CHOICE_CIVIL,null=True,blank=True) 
    destro = models.CharField('Destro',max_length=1,default='S',choices=CHOICE_SIM_NAO,null=True,blank=True) 
    endereco = models.CharField(u'Endereço',max_length=100,null=True,blank=True) 
    bairro = models.CharField('Bairro',max_length=60,null=True,blank=True) 
    complemento = models.CharField('Complemento',max_length=100,null=True,blank=True) 
    cidade = models.CharField('Cidade',max_length=100,null=True) 
    cep = models.CharField('Cep',max_length=10,null=True,blank=True) 
    foneresidencial = models.CharField(u'Telefone Residêncial',max_length=13,null=True,blank=True) 
    celular = models.CharField('Celular',max_length=13,null=True,blank=True) 
    email = models.CharField('E-Mail',max_length=80,null=True,blank=True) 
    dth_cadastro = models.DateTimeField(verbose_name='Data de Cadastro', auto_now_add=True)
    class Meta:
        verbose_name = u'Pessoa'
        verbose_name_plural = u'Pessoas'
    def __unicode__(self): 
        return self.nome    

class Avaliador(Pessoa):
    refFuncional=models.CharField(max_length=20, unique=True)
    turma = models.ManyToManyField(Turma)
    class Meta:
        verbose_name = u'Avaliador'
        verbose_name_plural = u'Avaliadores'
    def __unicode__(self): 
        return self.refFuncional 

class Avaliado(Pessoa):
    matricula=models.CharField(max_length=20, unique=True, verbose_name=u'Matrícula')
    turma = models.ManyToManyField(Turma)
    class Meta:
        verbose_name = u'Avaliado'
        verbose_name_plural = u'Avaliados'
    def __unicode__(self): 
        return self.matricula
    
class Usuario(models.Model):
    pessoa=models.ManyToManyField(Pessoa)
    login = models.CharField(max_length = 20, unique=True)
    password = models.CharField('Senha de Acesso',max_length = 20)
    perfil = models.CharField(max_length = 1, blank=True, null=True,choices=CHOICE_PERFIL) #A-Admin, U-Aluno, C-Consulta
    blk = models.BooleanField(verbose_name="Ativo", default=True) #Bloqueio de acesso
    class Meta:
        verbose_name = u'Usuário'
        verbose_name_plural = u'Usuários'
    def __unicode__(self): 
        return self.login 
     
class Grupo(models.Model):
    nome = models.CharField(max_length = 100, unique=True)
    usuario = models.ManyToManyField(Usuario)
    class Meta:
        verbose_name = u'Grupo'
        verbose_name_plural = u'Grupos'
    def __unicode__(self): 
        return self.nome 
    
    
