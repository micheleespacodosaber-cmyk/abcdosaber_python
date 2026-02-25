from django import forms

class TituloForm(forms.Form):
    descricao = forms.CharField(max_length=100, required=False, help_text='Informe o título')