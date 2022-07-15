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
    post.Counted_view += 1
    post.save()

    posts= Post.objects.filter(Status= True)
    posts= list(posts.reverse())
    post_in_posts= posts.index(post)
    if posts[post_in_posts] == posts[-1]:
        previous_post= posts[post_in_posts - 1]
        next_post= None
    elif posts[post_in_posts] == posts[0]:
        previous_post= None
        next_post= posts[post_in_posts + 1]

    else:
        previous_post= posts[post_in_posts - 1]
        next_post= posts[post_in_posts + 1]

    Context= {'post':post, 'nextpost':next_post, 'previouspost': previous_post}
    return render(request, 'blog/blog-single.html', Context)