from sageowl.usuarios.models import Usuario
from sageowl.usuarios.models import Grupo
from sageowl.usuarios.models import Pessoa
from sageowl.usuarios.models import Avaliador
from sageowl.usuarios.models import Avaliado

from django.contrib import admin

admin.site.register(Usuario)
admin.site.register(Grupo)
admin.site.register(Pessoa)
admin.site.register(Avaliador)
admin.site.register(Avaliado)