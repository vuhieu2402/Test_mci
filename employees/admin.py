from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display = ('name', 'position', 'email')
    search_fields = ['name', 'email']
    list_filter = ('position',)