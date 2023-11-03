from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q

from .forms import TaskForm
from .models import Task


@login_required(login_url="/login")
def insert_task(request):
    if request.method == 'POST':
        today_date = timezone.now().date()
        # Filter the queryset based on the date
        task_count = Task.objects.filter(author_id=request.user.id, created_date__date=today_date).count()
        if task_count >= 5:
            messages.error(request, 'Sorry, You have reached the maximum number of tasks(5 tasks) which can be '
                                    'added in one day. Delete an existing task or Try again tomorrow.')
            return redirect('account:home')

        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            messages.success(request, 'Task Created.')
            return redirect('account:home')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {"form": form})


@login_required(login_url="/login")
def details_task(request, id):
    task = Task.objects.get(pk=id)
    context = {'task': task}
    return render(request, 'tasks/task_view.html', context)


@login_required(login_url="/login")
def modify_task(request, id):
    obj_to_update = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=obj_to_update)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Updated.')
            return redirect('account:home')
    else:
        form = TaskForm(instance=obj_to_update)
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required(login_url="/login")
def destroy_task(request, id):
    Task.objects.get(pk=id).delete()
    messages.error(request, 'Task Deleted.')
    return redirect('account:home')


def search_tasks(request, key):
    tasks = Task.objects.filter(
        Q(title__icontains=key) | Q(description__icontains=key),
        author_id=request.user.id
    ).order_by('title')
    tasks = [a.as_json() for a in tasks]
    response = {"tasks": tasks}
    csrf_token = get_token(request)
    response['csrf_token'] = csrf_token
    return JsonResponse(response, safe=False)


def filter_tasks(request, status):
    tasks = Task.objects.filter(author_id=request.user.id, status=status).order_by('title')
    tasks = [a.as_json() for a in tasks]
    response = {"tasks": tasks}
    csrf_token = get_token(request)
    response['csrf_token'] = csrf_token
    return JsonResponse(response, safe=False)
