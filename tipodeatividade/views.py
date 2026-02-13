from django.shortcuts import render
from django.http import HttpResponse
from tipodeatividade.models import TipoDeAtividade
from tipodeatividade.forms import TipoDeAtividadeForm 


# Create your views here.
def listar(request):
    lista_tipodeatividade = TipoDeAtividade.objects.all()
    contexto = {
        'tiposdeatividade': lista_tipodeatividade
    }

    return render(request, 'tipodeatividade/listarTiposAtividade.html', context=contexto)

def carregar_cadastro(request):
    return render(request, 'tipodeatividade/cadastroTipoDeAtividade.html')


def cadastrar(request):
    form = TipoDeAtividadeForm(request.POST)
    if form.is_valid():
        dados_tipodeatividade = form.cleaned_data
        tipodeatividade = TipoDeAtividade(
            descricao=dados_tipodeatividade['descricao']
        )

        tipodeatividade.save()
return render(request, 'tipodeatividade/cadastroTipoDeAtividade.html')
