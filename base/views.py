from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import TodoItem
from .forms import TodoItemForm

def index(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoItemForm()

    todo_items = TodoItem.objects.all()
    return render(request, 'base/index.html', {'todo_items': todo_items, 'form': form})

def update_todo(request, pk):
    todo_item = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoItemForm(instance=todo_item)
    return render(request, 'base/update_todo.html', {'form': form})

def delete_todo(request, pk):
    todo_item = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        todo_item.delete()
        return redirect('index')
    return render(request, 'base/delete_todo.html', {'todo_item': todo_item})