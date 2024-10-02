from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import Todo


# Home Page
def home(request):
    if request.method == "POST":
        todo_id = request.POST.get("todo_id")
        if todo_id:
            todo = get_object_or_404(Todo, id=todo_id)
            todo.completed = not todo.completed
            todo.save()
            return redirect("home")

    todos = Todo.objects.all()
    return render(request, "base/home.html", {"todos": todos})


# Creating or Adding a Task
def add_todo(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            messages.error(request, "something wrong...")
    else:
        form = TodoForm()

    return render(request, "base/add_todo.html", {"form": form})


# Updating the Task
def update_todo(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            messages.error(request, "something went wrong please check the form")
    else:
        form = TodoForm(instance=todo)
    
    return render(request, "base/add_todo.html", {"form": form, "todo": todo})