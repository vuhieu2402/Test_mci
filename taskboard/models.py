from django.db import models
from employees.models import Employee

# Create your models here.

class Task(models.Model):

    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='tasks')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='todo')
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title