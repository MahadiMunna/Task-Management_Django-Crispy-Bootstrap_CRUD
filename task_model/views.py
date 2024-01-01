from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskModelForm

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = TaskModelForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    else:
        task_form = TaskModelForm()
    return render(request, 'add_task.html', {'form': task_form})

def edit_task(request, id):
    task = TaskModel.objects.get(id=id)
    task_form = TaskModelForm(instance=task)
    if request.method == 'POST':
        task_form = TaskModelForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    return render(request, 'edit_task.html', {'form': task_form})

def delete_task(request, id):
    TaskModel.objects.get(id=id).delete()
    return redirect('home')