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




