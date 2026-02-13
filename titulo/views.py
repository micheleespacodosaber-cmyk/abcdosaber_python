from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Titulo

# Create your views here.
def listar(request):
    lista_titulo = Titulo.objects.all()
    contexto = {
        'titulos': lista_titulo
    }

    return render(request, 'titulo/listarTitulos.html', context=contexto)
def carregar_titulo(request):
    return render(request, 'titulo/cadastrotitulo.html')

