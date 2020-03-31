from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Task


def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)


def add_task(request: HttpRequest):
    task = Task(title=request.POST['title'])
    task.save()
    return redirect('/tasks')


def del_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks')
