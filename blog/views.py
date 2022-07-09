from django.shortcuts import render
from blog.models import Post
# Create your views here.

def index(request):
    Posts= Post.objects.filter()
    Context= {"Posts": Posts}
    return render(request, 'blog/blog-home.html', Context)


def single(request):
    return render(request, 'blog/blog-single.html')