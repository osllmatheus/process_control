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
        fields = ('nome_subprocesso','status','processo','parent')
    
    parent = forms.ModelChoiceField(
        queryset=SubProcesso.objects.all(),
        required=False,
        label="Subprocesso Parent",
        empty_label="-----"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].queryset = SubProcesso.objects.all().order_by('lft')  # Ordena os subprocessos por ordem de árvore