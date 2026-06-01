from django.shortcuts import render , redirect
from .models import Task

# Create your views here.
def index(request):
    context = {
        "task":Task.objects.all()
    }
    return render(request,"index.html",context)

def new(request):
    return render(request,"new.html")

def create(request):
    Task.objects.create(
        title = request.POST["title"],
        description = request.POST["description"],
        is_completed = "is_completed" in request.POST
    )
    return redirect("/")

def show(request, id):
    context = {
        "task":Task.objects.get(id = id)
    }
    return render(request,"show.html",context)

def edit(request, id):
    context = {
        "task":Task.objects.get(id = id)
    }
    return render(request,"edit.html",context)

def update(request, id):
    task = Task.objects.get(id=id)
    task.title = request.POST["title"]
    task.description = request.POST["description"]
    task.is_completed = "is_completed" in request.POST
    task.save()
    return redirect("/")

def delete(request,id):
    id = request.POST['task_id']
    task = Task.objects.get(id = id)
    task.delete()
    return redirect("/")


    