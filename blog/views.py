from django.http import HttpResponse
from django.shortcuts import render

posts = {
    "first-post": "blah blah blah"
}
# Create your views here.

def index(request):
    return HttpResponse("index page")

def post(request):
    return HttpResponse("blog page")

