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
                                    ).distinct()
    
    estrutura_processos = {}
    
    num_subprocessos = 0
    num_pendentes = 0
    num_andamento = 0
    for processo in processos:
        todos_os_subprocessos = SubProcesso.objects.filter(processo=processo).get_descendants(include_self=True)
        estrutura_processos[processo] = todos_os_subprocessos
        num_subprocessos += processo.subprocessos.all().get_descendants(include_self=True).count()
        num_pendentes += processo.subprocessos.all().get_descendants(include_self=True).filter(status='P').count()
        num_andamento += processo.subprocessos.all().get_descendants(include_self=True).filter(status='A').count()

    num_processos = processos.count()

    return render(request, 'dashboard/index.html', {
        'form': form,
        'estrutura_processos':estrutura_processos,
        'num_processos': num_processos,
        'num_andamento': num_andamento,
        'num_subprocessos': num_subprocessos,
        'num_pendentes': num_pendentes,
    })
