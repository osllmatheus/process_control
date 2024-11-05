from django.db import models

class Area(models.Model):
    nome_area = models.CharField(max_length=200,null=False, blank=False)

    def __str__(self):
        return self.nome_area
