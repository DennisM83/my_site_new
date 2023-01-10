from django.http import HttpResponse
from django.shortcuts import render

post = {
    "first-post": "blah blah blah"
}
# Create your views here.

def index(request):
    return HttpResponse("index page")

def posts(request):
    return HttpResponse("blog posts")

