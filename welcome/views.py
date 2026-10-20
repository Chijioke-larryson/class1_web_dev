from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse("Hello Testimony!!!")
def john(request):
    return HttpResponse("Hello John!!!")

def status(request,status):
    return HttpResponse(f"You are offline {status}")
