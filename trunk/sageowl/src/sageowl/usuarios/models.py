from django.db import models
from django.utils.translation import ugettext as _ 
from django.conf import settings       
import datetime 

CHOICE_SEXO =(
    ('Homem'    ,  'M'),
    ('Mulher'      ,  'F'  ),
)

CHOICE_ESTADO =(
    ('Minas Gerais'      ,  'MG'  ),
    ('Rio de Janeiro'    ,  'RJ'),
    ('Sao Paulo'      ,  'SP'  ),
)

CHOICE_CIVIL =(
    ('Casado'      ,  'C'  ),
    ('Solteiro'    ,  'S'),
    ('Divorciado'      ,  'D'  ),
)

CHOICE_SIM_NAO =(
    ('Sim'      ,  'S'  ),
    ('Nao'      ,  'N'  ),
) 
   
class Usuario(models.Model):
    login = models.CharField(max_length = 20, unique=True)
    password = models.CharField('Senha de Acesso',max_length = 20)
    perfil = models.CharField(max_length = 1, blank=True, null=True) #A-Admin, U-Aluno, C-Consulta
    blk = models.BooleanField(verbose_name="Ativo", default=True) #Bloqueio de acesso
    dt_cadastro = models.DateTimeField(verbose_name='Data de Cadastro', auto_now_add=True) 
    class Meta:
        verbose_name = u'Usuario'
        verbose_name_plural = u'Usuarios'
    def __unicode__(self): 
        return self.login 
     
class Grupo(models.Model):
    nome = models.CharField(max_length = 100, unique=True)
    usuarios = models.ManyToManyField(Usuario)
    class Meta:
        verbose_name = u'Grupo'
        verbose_name_plural = u'Grupos'
    def __unicode__(self): 
        return self.nome 
    
class Pessoa(Usuario): 
    nome = models.CharField('Nome',max_length=100) 
    mae = models.CharField('Nome da Mae',max_length=100) 
    pai = models.CharField('Nome do Pai',max_length=100,null=True,blank=True) 
    dt_nasc = models.DateField('Data de Nascimento') 
    naturalidade = models.CharField('Naturalicade',max_length=100) 
    nacionalidade = models.CharField('Nacionalidade',max_length=100)
    sexo = models.CharField('Sexo',max_length=1,default='M',choices=CHOICE_SEXO) 
    rg = models.CharField('RG',max_length=25) 
    rgorgexp = models.CharField('Orgao Expedidor',max_length=15) 
    uf = models.CharField('UF',max_length=2,choices=CHOICE_ESTADO) 
    cpf = models.CharField('CPF',max_length=11,null=True,blank=True) 
    estadocivil = models.CharField('Estado Civil',max_length=1,choices=CHOICE_CIVIL) 
    destro = models.CharField('Destro',max_length=1,default='S',choices=CHOICE_SIM_NAO) 
    endereco = models.CharField('Endereco',max_length=100) 
    bairro = models.CharField('Bairro',max_length=60) 
    complemento = models.CharField('Complemento',max_length=100,null=True,blank=True) 
    cidade = models.CharField('Cidade',max_length=100) 
    cep = models.CharField('Cep',max_length=10,null=True,blank=True) 
    foneresidencial = models.CharField('Telefone Residencial',max_length=13,null=True,blank=True) 
    celular = models.CharField('Celular',max_length=13,null=True,blank=True) 
    email = models.CharField('E-Mail',max_length=80,null=True,blank=True) 
    dt_cadastro = models.DateTimeField(verbose_name='Data de Cadastro', auto_now_add=True)
    class Meta:
        verbose_name = u'Pessoa'
        verbose_name_plural = u'Pessoas'
    def __unicode__(self): 
        return self.nome 
    
class Avaliador(Pessoa):
    refFuncional=models.CharField(max_length=20, unique=True)
    class Meta:
        verbose_name = u'Avaliador'
        verbose_name_plural = u'Avaliadores'
    def __unicode__(self): 
        return self.refFuncional 

class Avaliado(Pessoa):
    matricula=models.CharField(max_length=20, unique=True)
    class Meta:
        verbose_name = u'Avaliado'
        verbose_name_plural = u'Avaliados'
    def __unicode__(self): 
        return self.matricula
    
