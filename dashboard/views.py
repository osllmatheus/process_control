from django.shortcuts import render
from processo.models import Processo
from processo.models import SubProcesso
from area.models import Area

def dashboard(request):
    processos = Processo.objects.all().select_related('area').prefetch_related('subprocesso')

    num_processos = processos.count()
    num_areas = Area.objects.count()
    num_subprocessos = SubProcesso.objects.count()

    return render(request, 'dashboard/index.html', {
        'processos': processos,
        'num_processos': num_processos,
        'num_areas': num_areas,
        'num_subprocessos': num_subprocessos, 
    })
