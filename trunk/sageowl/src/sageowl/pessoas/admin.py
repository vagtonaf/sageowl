from sageowl.pessoas.models import Pessoa
from sageowl.pessoas.models import Avaliador
from sageowl.pessoas.models import Avaliado
from sageowl.pessoas.models import Usuario
from sageowl.pessoas.models import Grupo

from django.contrib import admin

admin.site.register(Pessoa)
admin.site.register(Avaliador)
admin.site.register(Avaliado)
admin.site.register(Usuario)
admin.site.register(Grupo)
