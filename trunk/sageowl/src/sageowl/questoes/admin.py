from sageowl.questoes.models import Classificacao
from sageowl.questoes.models import Taxionomia
from sageowl.questoes.models import Questao
from sageowl.questoes.models import QuestaoDiscurssiva
from sageowl.questoes.models import QuestaoObjetiva
from sageowl.questoes.models import Alternativa
 
from django.contrib import admin

class QuestaoAdmin(admin.ModelAdmin):
    [
        (None,    {'fields': ['texto']}),
        ('valor', {'fields': ['valor']}),
        ('classificacao', {'fields': ['classificacao'],'classes': ['collapse']}),
    ]
    list_display = ('texto', 'valor', 'classificacao')


admin.site.register(Classificacao)
admin.site.register(Taxionomia)
admin.site.register(Questao, QuestaoAdmin)
admin.site.register(QuestaoDiscurssiva)
admin.site.register(QuestaoObjetiva)
admin.site.register(Alternativa)