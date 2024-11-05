from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Processo,SubProcesso
from .forms import ProcessoForm, SubProcessoForm

def processo_list(request):
    processo = Processo.objects.all()
    return render(request, 'processo/processo_list.html', {'processos':processo})

def processo_detail(request,pk):
    processo = get_object_or_404(Processo, pk=pk)
    return render(request, 'processo/processo_detail.html', {'processo': processo})

def processo_new(request):
    if request.method == "POST":
        form = ProcessoForm(request.POST)
        if form.is_valid():
            processo = form.save(commit=True)
            processo.save()
            return redirect('processo_detail', pk=processo.pk)
    else:
        form = ProcessoForm()
    return render(request, 'processo/processo_edit.html', {'form': form})

def processo_edit(request,pk):
    processo = get_object_or_404(Processo, pk=pk)
    if request.method == "POST":
        form = ProcessoForm(request.POST, instance=processo)
        if form.is_valid():
            processo = form.save(commit=True)
            processo.save()
            return redirect('processo_detail', pk=processo.pk)
    else:
        form = ProcessoForm(instance=processo)
    return render(request, 'processo/processo_edit.html', {'form': form})

def processo_delete(request,pk):
    processo = get_object_or_404(Processo,pk=pk)
    if request.method == "POST":
        processo.delete()
        return redirect('processo_list')
    return render(request, 'processo/processo_confirm_delete.html', {'processo': processo})

def sub_processo_list(request):
    sub_processo = SubProcesso.objects.all()
    return render(request, 'processo/sub_processo_list.html', {'subprocessos':sub_processo})

def sub_processo_detail(request,pk):
    sub_processo = get_object_or_404(SubProcesso, pk=pk)
    return render(request, 'processo/sub_processo_detail.html', {'subprocesso': sub_processo})

def sub_processo_new(request):
    if request.method == "POST":
        form = SubProcessoForm(request.POST)
        if form.is_valid():
            sub_processo = form.save(commit=True)
            sub_processo.save()
            return redirect('subprocesso_detail', pk=sub_processo.pk)
    else:
        form = SubProcessoForm()
    return render(request, 'processo/sub_processo_edit.html', {'form': form})

def sub_processo_edit(request,pk):
    sub_processo = get_object_or_404(SubProcesso, pk=pk)
    if request.method == "POST":
        form = SubProcessoForm(request.POST, instance=sub_processo)
        if form.is_valid():
            sub_processo = form.save(commit=True)
            sub_processo.save()
            return redirect('subprocesso_detail', pk=sub_processo.pk)
    else:
        form = SubProcessoForm(instance=sub_processo)
    return render(request, 'processo/sub_processo_edit.html', {'form': form})

def sub_processo_delete(request,pk):
    sub_processo = get_object_or_404(SubProcesso,pk=pk)
    if request.method == "POST":
        sub_processo.delete()
        return redirect('subprocesso_list')
    return render(request, 'processo/sub_processo_confirm_delete.html', {'subprocesso': sub_processo})