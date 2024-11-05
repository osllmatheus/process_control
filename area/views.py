from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Area
from .forms import AreaForm

def area_list(request):
    area = Area.objects.all()
    return render(request, 'area/area_list.html', {'areas':area})

def area_detail(request,pk):
    area = get_object_or_404(Area, pk=pk)
    return render(request, 'area/area_detail.html', {'area': area})

def area_new(request):
    if request.method == "POST":
        form = AreaForm(request.POST)
        if form.is_valid():
            area = form.save(commit=False)
            area.save()
            return redirect('area_detail', pk=area.pk)
    else:
        form = AreaForm()
    return render(request, 'area/area_edit.html', {'form': form})

def area_edit(request,pk):
    area = get_object_or_404(Area, pk=pk)
    if request.method == "POST":
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            area = form.save(commit=False)
            area.save()
            return redirect('area_detail', pk=area.pk)
    else:
        form = AreaForm(instance=area)
    return render(request, 'area/area_edit.html', {'form': form})

def area_delete(request,pk):
    area = get_object_or_404(Area,pk=pk)
    if request.method == "POST":
        area.delete()
        return redirect('area_list')
    return render(request, 'area/area_confirm_delete.html', {'area': area})