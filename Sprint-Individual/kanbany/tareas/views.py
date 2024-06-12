from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Tarea, Etiqueta, Prioridad
from .forms import TareaForm

# Create your views here.
@login_required
def tarea_list(request):
    tareas = Tarea.objects.filter(usuario=request.user).order_by('fecha_vencimiento')
    return render(request, 'tareas/list.html', {'tareas': tareas})

@login_required
def tarea_create(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.asignado_a = request.POST.get('asignado_a')
            tarea.save()
            return redirect('tarea_list')
    else:
        form = TareaForm()
        usuarios = User.objects.all()
    return render(request, 'tareas/create.html', {'form': form})

@login_required
def tarea_edit(request, pk):
    tarea = Tarea.objects.get(pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tarea_list')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/edit.html', {'form': form})

@login_required
def tarea_delete(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tarea_list')
     return render(request, 'tareas/delete.html', {'tarea': tarea})

@login_required
def tarea_detail(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, 'tasks/detail.html', {'tarea': tarea})

