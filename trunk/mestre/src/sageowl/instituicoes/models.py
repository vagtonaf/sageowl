# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _ 
from django.conf import settings       
import datetime 

CHOICE_TURNO=(
    ('M'      ,  u'Manhã'  ),
    ('T'      ,  'Tarde'  ),
    ('N'      ,  'Noite'  ),
) 

class Instituicao(models.Model):
    nome = models.CharField(max_length = 150, unique=True)
    class Meta:
        verbose_name = u'Instituição'
        verbose_name_plural = u'Instituições'
    def __unicode__(self): 
        return self.nome

class Curso(models.Model):
    instituicao=models.ForeignKey(Instituicao)
    referencia=models.CharField(max_length = 20, unique=True, verbose_name=u'Referência')
    nome = models.CharField(max_length = 150)
    class Meta:
        unique_together = ('instituicao','referencia')
        verbose_name = u'Curso'
        verbose_name_plural = u'Cursos'
    def __unicode__(self): 
        return self.nome

class Disciplina(models.Model):
    curso=models.ForeignKey(Curso)
    referencia = models.CharField(max_length = 20, unique=True, verbose_name=u'Referência')
    nome = models.CharField(max_length = 150)
    class Meta:
        unique_together = ('curso','referencia')
        verbose_name = u'Disciplina'
        verbose_name_plural = u'Disciplinas'
    def __unicode__(self): 
        return self.nome
    
class Turma(models.Model):
    disciplina=models.ForeignKey(Disciplina)
    referencia = models.CharField(max_length = 20, unique=True, verbose_name=u'referência')
    turno = models.CharField('Turno',max_length=1,default='M',choices=CHOICE_TURNO) 
    class Meta:
        unique_together = ('disciplina','referencia')
        verbose_name = u'Turma'
        verbose_name_plural = u'Turmas'
    def __unicode__(self): 
        return self.referencia
