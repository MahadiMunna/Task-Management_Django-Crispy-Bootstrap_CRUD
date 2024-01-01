from django import forms
from .models import TaskModel

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'

        widgets = {
            'assignDate': forms.DateInput({'type':'date'})
        }

        labels = {
            'taskTitle':'Enter the task title',
            'taskDescription':'Write the task description',
            'is_completed':'Is the task completed?',
            'assignDate':'When the task is assigned?'
        }