from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")
# Create your views here.
def greet(request, name):
    return HttpResponse("Hello, "+name.capitalize())