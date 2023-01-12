from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello from the home page!")

def about(request):
    return HttpResponse("About page")

def contact(request):
    return HttpResponse("Contact Page")