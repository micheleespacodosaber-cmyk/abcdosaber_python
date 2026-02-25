from django.shortcuts import render, redirect
from django.http import HttpResponse
from instrutor.models import Instrutor
from instrutor.forms import InstrutorForm


# Create your views here.
def listar(request):
    lista_instrutor = Instrutor.objects.all()
    contexto = {
        'instrutores': lista_instrutor
    }

    return render(request, 'instrutor/listarInstrutor.html', context=contexto)

def carregar_cadastro(request):
    form = InstrutorForm()
    return render(request, 'instrutor/cadastroInstrutor.html', {'form': form})


def cadastrar_instrutor(request):
    if request.method == 'POST':
        form = InstrutorForm(request.POST)  
        if form.is_valid():  
            dados_instrutor = form.cleaned_data
            instrutor = Instrutor(
                descricao=dados_instrutor['descricao']
            )
            instrutor.save()
            return redirect('instrutor:listar')  
    else:
        form = InstrutorForm()

    return render(request, 'instrutor/cadastroInstrutor.html', {'form': form})