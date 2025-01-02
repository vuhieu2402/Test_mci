from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
