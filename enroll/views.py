from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Todo
from .models import TodoList
import json
# Create your views here.


def home(request):
    colors = ['success', 'danger', 'primary']

    todos = list(TodoList.objects.all())
    ids = [i.id for i in todos]
    todos = list(map(lambda x: json.loads(str(x).replace("'", '"')), todos))
    colors = [colors[i % 3] for i in range(len(todos))]

    colors = zip(todos, colors, ids)

    if request.method == "POST":
        td = Todo(request.POST)
        if td.is_valid():
            res = {'todo': td.cleaned_data['todo'],
                   'time': str(td.cleaned_data['time']).replace('T', ' ')}
            newdata = TodoList(todo=res.get('todo'), time=res.get('time'))
            newdata.save()
            colors = ['success', 'danger', 'primary']

            todos = list(TodoList.objects.all())
            ids = [i.id for i in todos]
            todos = list(map(lambda x: json.loads(
                str(x).replace("'", '"')), todos))
            colors = [colors[i % 3] for i in range(len(todos))]

            colors = zip(todos, colors, ids)
            return render(request, 'enroll/html/home.html', {'fo': colors, 'fm': td, 'data': todos})
    td = Todo()
    # print(json.loads(str(TodoList.objects.all()[0]).replace("'", '"')))
    return render(request, 'enroll/html/home.html', {'fo': colors, 'fm': td, 'data': todos})


def delete(request, id):
    reg = TodoList.objects.filter(id=id)
    reg.delete()
    return redirect(home)


def edit(request, id):
    person = TodoList.objects.filter(id=id).first()
    person = json.loads(str(person).replace("'", '"'))
    if request.method == "POST":

        data = str(dict(request.POST)).replace(
            '[', '').replace(']', '').replace("'", '"')
        data = json.loads(data)
        print(data.get('submit'))
        if data.get('submit'):
            reg = TodoList(id=id, todo=data.get('todo'),
                           time=data.get('time').replace('T', ' '))
            reg.save()
        return redirect(home)
    return render(request, "enroll/html/edit.html", {'id': id, 'todo': person.get('todo'), 'time': person.get('time').replace(' ', 'T')})
