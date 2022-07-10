from django.shortcuts import render
from blog.models import Post
from datetime import datetime
# Create your views here.

def index(request):
    Current_Time = datetime.now()
    posts= Post.objects.filter(Published_Date__lte= Current_Time)
    for post in posts:
        post.Status= True
    Context= {"posts": posts}
    return render(request, 'blog/blog-home.html', Context)


def single(request):
    def Add_View(post):
        post.Counted_view += 1
    # Because of we do not have any auther yet, we can not use Add_View
    return render(request, 'blog/blog-single.html')