from django.db import models
from area.models import Area
from django.core.exceptions import ValidationError
    
class SubProcesso(models.Model):
    nome_subprocesso = models.CharField(max_length=200)
    parent_subprocesso = models.ManyToManyField('self', symmetrical=False, related_name='subprocessos_filhos', blank=True)

    def __str__(self):
        return self.nome_subprocesso
    
class Processo(models.Model):
    nome_processo = models.CharField(max_length=200)
    ferramenta_utilizada = models.CharField(max_length=400)
    responsavel = models.CharField(max_length=400)
    documentacao = models.CharField(max_length=400)
    subprocesso = models.ManyToManyField(SubProcesso, related_name='processos', blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE,null=True, blank=True, related_name='processos')

    def __str__(self):
        return self.nome_processo