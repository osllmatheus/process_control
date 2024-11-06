from django import forms

from .models import Processo, SubProcesso

class ProcessoForm(forms.ModelForm):

    class Meta:
        model = Processo
        fields = ('nome_processo','ferramenta_utilizada',
                  'responsavel','documentacao','area')
        widgets = {
            'subprocesso' : forms.CheckboxSelectMultiple,
        }
        
class SubProcessoForm(forms.ModelForm):
    class Meta:
        model = SubProcesso
        fields = ('nome_subprocesso','parent_subprocesso')
        widgets = {
            'parent_subprocesso' : forms.CheckboxSelectMultiple,
        }