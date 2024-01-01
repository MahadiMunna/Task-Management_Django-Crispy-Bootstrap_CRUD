from django.shortcuts import render, redirect
from .forms import TaskCategoryForm


# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category_form = TaskCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('home')
    else:
        category_form = TaskCategoryForm()
    return render(request, 'add_category.html', {'form': category_form})
