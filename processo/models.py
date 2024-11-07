from django.db import models
from django.core.exceptions import ValidationError
from mptt.models import MPTTModel, TreeForeignKey
from area.models import Area

# Modelo SubProcesso
class SubProcesso(MPTTModel):
    nome_subprocesso = models.CharField(max_length=200)
    processo = models.ForeignKey('Processo', related_name='subprocessos', on_delete=models.CASCADE, null=True, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='subprocessos_filhos', on_delete=models.CASCADE)


    STATUS_OPCOES = [
        ('P', 'Pendente'),
        ('A', 'Em Andamento'),
        ('C', 'Concluído'),
        ('X', 'Cancelado'),
    ]
    
    status = models.CharField(
        max_length=1,
        choices=STATUS_OPCOES,
        default='P',
    )
    
    class MPTTMeta:
        order_insertion_by = ['nome_subprocesso']  # Pode ordenar os subprocessos na árvore

    
    def clean(self):
        if self.processo and self.parent:
            raise ValidationError("Subprocesso com um processo não pode ter filhos com processo.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_subprocesso


# Modelo Processo
class Processo(models.Model):
    nome_processo = models.CharField(max_length=200)
    ferramenta_utilizada = models.CharField(max_length=400)
    responsavel = models.CharField(max_length=400)
    documentacao = models.CharField(max_length=400)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='processos')

    def __str__(self):
        return self.nome_processo
