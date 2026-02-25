from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Titulo
from .forms import TituloForm


# Create your views here.
def listar(request):
    lista_titulo = Titulo.objects.all()
    contexto = {
        'titulos': lista_titulo
    }
    return render(request, 'titulo/listarTitulos.html', context=contexto)

def carregar_titulo(request):
    return render(request, 'titulo/cadastrotitulo.html')

def cadastrar(request):
    form = TituloForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
        titulo = Titulo(
            descricao=dados_titulo['descricao']
        )

        titulo.save()
    return render(request, 'titulo/cadastroTitulo.html')


