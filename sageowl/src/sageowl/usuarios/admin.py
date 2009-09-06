from sageowl.usuarios.models import Pessoa
from sageowl.usuarios.models import Avaliador
from sageowl.usuarios.models import Avaliado
from sageowl.usuarios.models import Usuario
from sageowl.usuarios.models import Grupo

from django.contrib import admin

admin.site.register(Pessoa)
admin.site.register(Avaliador)
admin.site.register(Avaliado)
admin.site.register(Usuario)
admin.site.register(Grupo)
