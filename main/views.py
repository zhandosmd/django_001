from django.shortcuts import render, redirect

from main.forms import TaskForm
from .models import Task
from .forms import TaskForm



def index(request):
    # tasks = Task.objects.all()
    tasks = Task.objects.order_by('-id')
    # tasks = Task.objects.order_by('id')[:1]

    return render(request, 'main/index.html', {'title': 'Main page of site', 'tasks': tasks})


def info(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form was incorrect'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)