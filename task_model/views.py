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