from django.db import models
from django.urls import reverse

# Create your models here.

class tipodeatividade(models.Model):
    """ Modelo representando um tipo de atividade"""
    codigo = models.IntegerField(primary_key=True,
                                 help_text='código do tipo de atividade')
    descricao = models.CharField(max_length=70, null=False,
                                 help_text='Informe a descrição do tipo de atividade')
    

    def _str_(self):
        return f'{self.codigo} {self.descricao}'