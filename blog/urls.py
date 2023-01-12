from django.urls import path
from . import views

urlpatterns = [
    path("blog", views.index, name="blog-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.single_post, name="single-post-page")
]