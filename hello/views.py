from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from datetime import datetime
def index(request):
    return render(request, "hello/home.html")

def is_christmas(request):
    today = datetime.now()
    context = {
        "is_christmas": True
        
    }
    return render(request, "hello/christmas.html", context)
  
   

def Jacob(request):
    return render(request, "hello/Jacob.html")


def Dorcas(request):
    return HttpResponse("Hello, Dorcas. ")


def welcome(request, name):
    return HttpResponse(f"Hello, {name.upper()} Welcome to my site.")