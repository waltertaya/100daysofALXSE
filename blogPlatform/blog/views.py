from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'home'
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'about'})
