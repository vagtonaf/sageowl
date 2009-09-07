from sageowl.instituicoes.models import Instituicao
from sageowl.instituicoes.models import Curso
from sageowl.instituicoes.models import Disciplina
from sageowl.instituicoes.models import Turma
 
from django.contrib import admin

admin.site.register(Instituicao)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Turma)
