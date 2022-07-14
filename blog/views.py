from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
# Create your views here.

def blog_index(request):
    Local_Time= timezone.localtime(timezone.now())
    posts= Post.objects.filter(Published_Date__lte= Local_Time)
    for post in posts:
        if not post.Status: post.Status= True
        post.save()
    Context= {"posts": posts}
    return render(request, 'blog/blog-home.html', Context)


def blog_single(request, pid):
    post= get_object_or_404(Post, pk = pid, Status= True)
    Context= {'post':post}
    return render(request, 'blog/blog-single.html', Context)