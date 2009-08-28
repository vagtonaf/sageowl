from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from sageowl.questoes.models import Questao


def index(request):
    ultima_questao_list = Questao.objects.all().order_by('-referencia')[:5]
    return render_to_response('questoes/index.html', {'ultima_questao_list': ultima_questao_list})

def detail(request, questao_id):
    p = get_object_or_404(Questao, pk=questao_id)
    return render_to_response('questoes/detail.html', {'questao': p})

#Criar em D:\www\django\templates\questoes\index.html

#{% if ultima_questao_list %}
#    <ul>
#    {% for questao in ultima_questao_list %}
#        <li>{{ questao.referencia }}</li>
#        <li>{{ questao.texto }}</li>
#        <li>{{ questao.valor }}</li>
#    {% endfor %}
#    </ul>
#{% else %}
#    <p>Nenhuma questoes encontrada.</p>
#{% endif %}

# lista as Questoes

#http://localhost:8000/questoes/
