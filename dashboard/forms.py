from django import forms
from processo.models import Processo
from processo.models import SubProcesso
from area.models import Area

class FiltroDashboardForm(forms.Form):
    area = forms.ModelChoiceField(queryset=Area.objects.all(), required=False, label="Área")
    processo = forms.ModelChoiceField(queryset=Processo.objects.all(), required=False, label="Processo")
    subprocesso = forms.ModelChoiceField(queryset=SubProcesso.objects.all(), required=False, label="Subprocesso")