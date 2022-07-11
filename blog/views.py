from django.shortcuts import render, get_object_or_404
from blog.models import Post
from datetime import datetime
# Create your views here.

def blog_index(request):
    Current_Time = datetime.now()
    posts= Post.objects.filter(Published_Date__lte= Current_Time)
    for post in posts:
        post.Status= True
    Context= {"posts": posts}
    return render(request, 'blog/blog-home.html', Context)


def blog_single(request, pid):
    post= Post.objects.get(id = pid)
    Context= {'post':post}
    return render(request, 'blog/blog-single.html', Context)