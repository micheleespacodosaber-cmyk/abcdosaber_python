from django import forms

class InstrutorForm(forms.Form):

    rg = forms.CharField(max_length=15, help_text='código do RG')
    nome = forms.CharField(max_length=70, help_text='Nome do instrutor')
    data_nascimento = forms.DateField(help_text='Data de nascimento')
    telefone = forms.CharField(max_length=9, help_text='Telefone para contato')
    ddd = forms.CharField(max_length=3, help_text='DDD do seu estado')
    codigo_titulo = forms.IntegerField(help_text='Título do instrutor')
