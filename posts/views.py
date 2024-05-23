from django.shortcuts import render
from .models import Post

# Create your views here.

def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/list.html', { 'posts': posts })

def postpage(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/page.html', { 'post': post })
    