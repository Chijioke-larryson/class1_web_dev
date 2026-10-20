from django.urls import path 
from .import views

urlpatterns = [

    path("", views.hello, name="hello"),
    path("john/", views.john, name= "john"),
    path("<str:status>/", views.status, name="status")
]