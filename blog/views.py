from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
from django.core.paginator import Paginator as pg, EmptyPage, PageNotAnInteger
# Create your views here.

def blog_index(request, **kwargs):
    Local_Time= timezone.localtime(timezone.now())
    posts= Post.objects.filter(Published_Date__lte= Local_Time)
    if kwargs.get('cat_name'):
        posts= posts.filter(Category__Name= kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts= posts.filter(Author__username= kwargs['author_username'])
    for post in posts:
        if not post.Status: post.Status= True
        post.save()

    posts= pg(posts, 2)
    page_number= request.GET.get('page')

    try:
        posts= posts.get_page(page_number)
    except PageNotAnInteger:
        posts= posts.get_page(1)
    except EmptyPage:
        posts= posts.get_page(posts.num_pages)

    Context= {"posts": posts}
    return render(request, 'blog/blog-home.html', Context)


def blog_single(request, pid):
    post= get_object_or_404(Post, pk = pid, Status= True)
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


def blog_category(request, cat_name):
    posts= Post.objects.filter(Status= True, Category__Name= cat_name)
    Context= {"posts": posts}
    return render(request, 'blog/blog-home.html', Context)


def blog_search(request):
    posts= Post.objects.filter(Status= True)
    if request.method == 'GET' and (search := request.GET.get('search')):
        posts= posts.filter(Content__contains= search)
    Context= {"posts": posts}
    return render(request, 'blog/blog-home.html', Context)


