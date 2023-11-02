from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'