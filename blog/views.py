from django.http import HttpResponse
from django.shortcuts import render

articles = {
    "First Post": "blah blah blah",
    "Second Post": "blah blah blah"
}

# Create your views here.

def index(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/posts.html", {
        "articles": articles
    })
    
def single_post(request):
    pass
    

