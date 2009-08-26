from questoes.models import Classificacao
from questoes.models import Questao
#from questoes.models import QuestaoDiscurssiva
#from questoes.models import QuestaoObjetiva
from questoes.models import Alternativa
 
from django.contrib import admin

admin.site.register(Classificacao)
admin.site.register(Questao)
#admin.site.register(QuestaoDiscurssiva, QuestaoObjetiva)
admin.site.register(Alternativa)

 