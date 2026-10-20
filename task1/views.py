from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewTaskForm
# Create your views here.

tasks = []

context = {"tasks": tasks }
def index(request):
    if "task" not in request.session:
        request.session["task"] = []

    return render(request, "task1/home.html", {
        "tasks": request.session["task"]
    })
    request.session["task"] = tasks
def task(request):
    return render(request, "task1/home.html", context)

def AboutUs(request):
    return render(request, "task1/AboutUs.html")

def add(request):
  

    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            tasks = form.cleaned_data["task"]
            # tasks.append(task)
            # context["tasks"] = tasks
        
        else:
            return render(request, "task1/Form.html",
                          {
                "form": form
            })
    return render(request, "task1/Form.html",{
        "form": NewTaskForm()
    })