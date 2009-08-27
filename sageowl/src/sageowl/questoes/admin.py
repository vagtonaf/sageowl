from sageowl.questoes.models import Classificacao
from sageowl.questoes.models import Nivel
from sageowl.questoes.models import Questao
from sageowl.questoes.models import QuestaoDiscurssiva
from sageowl.questoes.models import QuestaoObjetiva
from sageowl.questoes.models import Alternativa
 
from django.contrib import admin

admin.site.register(Classificacao)
admin.site.register(Nivel)
admin.site.register(Questao)
admin.site.register(QuestaoDiscurssiva)
admin.site.register(QuestaoObjetiva)
admin.site.register(Alternativa)