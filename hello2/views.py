from django.shortcuts import render
from django.http import HttpResponse

def greet(request, name):
    return HttpResponse("Hello, "+name.capitalize())
# Create your views here.
