from django.db import models

# Create your models here.


class TodoList(models.Model):
    todo = models.CharField(max_length=200)
    time = models.CharField(max_length=70)

    def __str__(self):
        return str(dict(todo=self.todo, time=self.time))
