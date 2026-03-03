from django.shortcuts import render, redirect
from django.http import HttpResponse
from instrutor.models import Instrutor
from instrutor.forms import InstrutorForm
from titulo.models import Titulo


# Create your views here.
def listar(request):
    lista_instrutor = Instrutor.objects.all()
    contexto = {
        'instrutores': lista_instrutor
    }

    return render(request, 'instrutor/listarInstrutor.html', context=contexto)

def carregar_cadastro(request):

    lista_titulos = Titulo.objects.all()
    contexto = { 
        'titulos': lista_titulos,
    }
    return render(request, 'instrutor/cadastroInstrutor.html',context=contexto)


def cadastrar(request):
    form = InstrutorForm(request.POST)  
    if form.is_valid():  
        dados_instrutor = form.cleaned_data
        instrutor = Instrutor(
            nome=dados_instrutor['nome'],
            rg=dados_instrutor['rg'],
            dataNascimento=dados_instrutor['data_nascimento'],
            ddd=dados_instrutor['ddd'],
            telefone=dados_instrutor['telefone'],
            codigo_titulo_id=dados_instrutor['codigo_titulo']
        )

        instrutor.save()
        return redirect('instrutor_listar')

    else:
        print(form.errors)

    return render(request, 'instrutor/cadastroInstrutor.html', context=contexto)