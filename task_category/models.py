from django.db import models
from task_model.models import TaskModel
# Create your models here.
class TaskCategory(models.Model):
    name = models.CharField(max_length=20)
    taskModel = models.ManyToManyField(TaskModel)

    def __str__(self) -> str:
        return self.name