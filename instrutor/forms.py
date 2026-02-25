from django import forms

class Instrutor(forms.Form):
    descricao = forms.CharField(max_length=100, required=False, help_text='Informe a descrição instrutor')

def cadastrar(request):
    form = InstrutorForm(request.POST)

    if form.is_valid():
        dados_instrutor = form.cleaned_data

        instrutor = Instrutor(
            rg = dados_instrutor['rg'],
            nome = dados_instrutor['nome'],
            dataNascimento = dados_instrutor['dataNascimento'],
            telefone = dados_instrutor['telefone'],
            ddd = dados_instrutor['ddd'],
            codigoTitulo =  Titulo.codigo,
        )

        instrutor.save()
    return render(request,'instrutor/cadastroInstrutor.html')