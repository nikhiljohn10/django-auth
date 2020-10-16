from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from todo.models import Task
from todo.forms import TaskForm


@login_required(login_url='/auth/login/')
def list_tasks(request):
    tasks = Task.objects.filter(manager=request.user).order_by('-added_date')
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.manager = request.user
            task.save()
    form = TaskForm()
    return render(request, 'list.html', {'tasks': tasks, 'form': form})

@login_required(login_url='/auth/login/')
def remove_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('list_tasks')

@login_required(login_url='/auth/login/')
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.toggleStatus()
    return redirect('list_tasks')
