from django.db import models

# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    assignDate = models.DateField()

    def __str__(self) -> str:
        return self.taskTitle