from django.shortcuts import render
from django.db.models import Prefetch, Q
from processo.models import Processo
from processo.models import SubProcesso
from area.models import Area
from .forms import FiltroDashboardForm

def dashboard(request):
    form = FiltroDashboardForm(request.GET)

    processos = Processo.objects.select_related('area').prefetch_related('subprocessos', 'subprocessos__subprocessos_filhos').all()

    if form.is_valid():
        area = form.cleaned_data.get('area')
        processo = form.cleaned_data.get('processo')
        subprocesso = form.cleaned_data.get('subprocesso')

        if area:
            processos = processos.filter(area=area)
        if processo:
            processos = processos.filter(nome_processo=processo.nome_processo)
        if subprocesso:
            processos = processos.filter(Q(subprocessos__nome_subprocesso=subprocesso) | 
                                        Q(subprocessos__subprocessos_filhos__nome_subprocesso=subprocesso)
                                    )
    
    num_areas = processos.values('area').distinct().count()
    num_subprocessos = processos.prefetch_related('subprocesso').count()
    num_processos = processos.count()
    
    return render(request, 'dashboard/index.html', {
        'form': form,
        'processos': processos,
        'num_processos': num_processos,
        'num_areas': num_areas,
        'num_subprocessos': num_subprocessos,
    })
