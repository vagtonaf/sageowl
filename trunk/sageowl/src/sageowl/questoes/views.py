from django.template import Context, loader
from sageowl.questoes.models import Questao

from django.http import HttpResponse

def index(request):
    ultima_questao_list = Questao.objects.all().order_by('-referencia')[:5]
    t = loader.get_template('questoes/index.html')
    c = Context({
        'ultima_questao_list': ultima_questao_list,
    })
    return HttpResponse(t.render(c))


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
