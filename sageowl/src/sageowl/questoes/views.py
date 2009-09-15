# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from sageowl.questoes.models import Questao

# Esta funcionando legal Vagton ele busca no template o listaQuestao.html
def index(request):
    ultima_questao_list = Questao.objects.all().order_by('-referencia')[:5]
    return render_to_response('questoes/listaQuestao.html', {'ultima_questao_list': ultima_questao_list})

def detail(request, questao_id):
    p = get_object_or_404(Questao, pk=questao_id)
    return render_to_response('questoes/detail.html', {'questao': p})

from sageowl.questoes.forms import FormQuestao

def CadQuestao(request):
    if request.method=='POST':
        form = FormQuestao(request.POST)
        if form.is_valid():
            pass
            # aqui vai o código para enviar o e-mail
            # veja mais em http://docs.djangoproject.com/en/dev/topics/email/
    else:
        form = FormQuestao()
    return render_to_response('questoes/questao.html', {'form': form})
