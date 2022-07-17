from django import template
from django.utils import timezone


from blog.models import Category, Post

register= template.Library()

@register.simple_tag(name= "View_Counter")
def View(pid):
    post= Post.objects.get(pk= pid)
    post.Counted_view += 1
    post.save()
    return post.Counted_view

@register.filter
def Short_Content(Content,Len= 35):
    return ' '.join(Content.split()[:Len]) + ' ...'

@register.inclusion_tag('blog/blog-latestposts.html')
def Latestposts():
    posts= Post.objects.filter(Status= True).order_by('-Published_Date')[:4]
    Context= {'posts': posts}
    return Context

@register.simple_tag
def Past_Time(Published_Date):
    Current_Time= timezone.localtime(timezone.now())
    past_time=  Current_Time - Published_Date
    past_days= past_time.days
    return str(past_days) + ' Days ago'
    
@register.inclusion_tag('blog/blog-PostCategories.html')
def Post_Categories():
    posts= Post.objects.filter(Status= True)
    categories= Category.objects.all()
    Category_Dict= dict()
    
    for category in categories:
        Category_Dict[category]= posts.filter(Category= category).count()

    return {'Category_Dict': Category_Dict}