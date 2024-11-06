from django import forms

from .models import Processo, SubProcesso

class ProcessoForm(forms.ModelForm):

    class Meta:
        model = Processo
        fields = ('nome_processo','ferramenta_utilizada',
                  'responsavel','documentacao','area')
        
class SubProcessoForm(forms.ModelForm):
    class Meta:
        model = SubProcesso
        fields = ('nome_subprocesso','status','processo','parent_subprocesso')