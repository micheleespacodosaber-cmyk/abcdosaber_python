from django.db import models
from titulo.models import Titulo

class Instrutor(models.Model):

    id = models.AutoField(primary_key=True, help_text='ID do instrutor')
    rg = models.CharField(max_length=15, null=False, help_text='código do RG')
    nome = models.CharField(max_length=70, null=False, help_text='Nome do instrutor')
    dataNascimento = models.DateField(null=False, help_text='Data de nascimento')
    telefone = models.CharField(max_length=9, null=False, help_text='Telefone para contato')
    ddd = models.CharField(max_length=3, null=False, help_text='DDD do seu estado')
    codigo_titulo = models.IntegerField(null=True, help_text='Título do instrutor')
    codigo_titulo = models.ForeignKey(Titulo, null=True, related_name='titulos', on_delete=models.SET_NULL,
                                      db_column='codigo_titulo',
                                      help_text='Título do instrutor')


    def __str__(self):
        return f"{self.id} - {self.nome}"