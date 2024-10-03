from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import TodoForm
from .models import Todo
from .forms import MyUserCreationForm
from django.contrib.auth.decorators import login_required



def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")

        user = authenticate(request, email=email, password = password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "email or password are incorrect...")

    return render(request, "base/login_page.html")


def logout_page(request):
    logout(request)
    return redirect("login")



def register_user(request):
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "There was an error processing your registration. Please try again.")
    else:
        form = MyUserCreationForm()
    return render(request, "base/register_page.html", {"form": form})



# Home Page
@login_required(login_url="login")
def home(request):
    if request.method == "POST":
        todo_id = request.POST.get("todo_id")
        if todo_id:
            todo = get_object_or_404(Todo, id=todo_id)
            todo.completed = not todo.completed
            todo.save()
            return redirect("home")

    todos = Todo.objects.filter(user=request.user)
    incomplete_todos = todos.filter(completed = False).count()
    return render(request, "base/home.html", {"todos": todos, "incomplete_todos": incomplete_todos})


# Creating or Adding a Task
@login_required(login_url="login")
def add_todo(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect("home")
        else:
            messages.error(request, "something wrong...")
    else:
        form = TodoForm()

    return render(request, "base/add_todo.html", {"form": form})


# Updating the Task
@login_required(login_url="login")
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


# Deleting a Task
@login_required(login_url="login")
def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        todo.delete()
        return redirect("home")

    return render(request, "base/delete_page.html", {"obj": todo})