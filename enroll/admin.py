from django.contrib import admin

from .models import TodoList

# Register your models here.


@admin.register(TodoList)
class modelAdmin(admin.ModelAdmin):
    list_display = ['id', 'todo', 'time']
