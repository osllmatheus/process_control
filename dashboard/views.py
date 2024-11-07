from django.shortcuts import render
from django.db.models import Prefetch, Q
from processo.models import Processo
from processo.models import SubProcesso
from area.models import Area
from .forms import FiltroDashboardForm

def contar_subprocessos(estrutura):
    """
    Função para contar o número total de subprocessos diretamente associados aos processos,
    sem entrar nos subprocessos filhos.
    
    :param estrutura: Dicionário contendo a estrutura dos processos e subprocessos.
    :return: Número total de subprocessos diretamente associados.
    """
    total_subprocessos = 0
    
    # Percorre cada processo na estrutura
    for nome_processo, dados in estrutura.items():
        # Conta os subprocessos diretamente associados ao processo (de nível 1)
        total_subprocessos += len(dados["subprocessos"])
    
    return total_subprocessos

def contar_subprocessos_pendente(estrutura):
    """
    Função para contar o número total de subprocessos com status 'Pendente'.
    
    :param estrutura: Dicionário contendo a estrutura dos processos e subprocessos.
    :return: Número total de subprocessos com status 'Pendente'.
    """
    total_pendente = 0
    
    # Percorre cada processo na estrutura
    for nome_processo, dados in estrutura.items():
        # Conta os subprocessos de nível 1 com status 'Pendente'
        total_pendente += contar_pendente_subprocessos(dados["subprocessos"])
    
    return total_pendente

def contar_pendente_subprocessos(subprocessos):
    """
    Função para contar subprocessos com status 'Pendente' dentro de uma lista de subprocessos.
    
    :param subprocessos: Lista de subprocessos a ser verificada.
    :return: Número total de subprocessos com status 'Pendente'.
    """
    total_pendente = 0
    
    # Verifica cada subprocesso
    for subprocesso in subprocessos:
        # Se o subprocesso tem status 'Pendente', conta ele
        if subprocesso.get("status") == "Pendente":
            total_pendente += 1
        
        # Conta também os subprocessos filhos
        total_pendente += contar_pendente_subprocessos(subprocesso["subprocessos"])
    
    return total_pendente


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
    
    
    num_areas = processos.values('area').distinct().count()
    num_processos = processos.count()
    #num_subprocessos = contar_subprocessos(processos_dic)
    #num_pendente = contar_subprocessos_pendente(processos_dic)

    processos = Processo.objects.all()  # Pega todos os processos

    # Para cada processo, obtemos todos os subprocessos (diretos e indiretos)
    estrutura_processos = {}
    for processo in processos:
        subprocessos = processo.subprocessos.all()  # subprocessos de nível 1
        todos_os_subprocessos = SubProcesso.objects.filter(processo=processo).get_descendants(include_self=True)
        estrutura_processos[processo.nome_processo] = todos_os_subprocessos


        
    subprocessos = SubProcesso.objects.all()
    return render(request, 'dashboard/index.html', {
        'form': form,
        'estrutura_processos':estrutura_processos,
        'processos' : processos,
        'subprocessos': subprocessos,
        'num_processos': num_processos,
        'num_areas': num_areas,
        #'num_subprocessos': num_subprocessos,
        #'num_pendente': num_pendente,
    })
