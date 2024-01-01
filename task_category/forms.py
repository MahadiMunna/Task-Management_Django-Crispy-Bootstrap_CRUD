from django import forms
from .models import TaskCategory

class TaskCategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = '__all__'

        labels = {
                'name':'Enter the name of category',
                'taskModel':'Select the tasks which are in this category'
            }
        widgets = {
                'taskModel': forms.CheckboxSelectMultiple()
            }