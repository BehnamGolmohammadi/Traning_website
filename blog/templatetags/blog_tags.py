from django import template
from django.utils import timezone


from blog.models import Post

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

@register.inclusion_tag('blog/blog-popularposts.html')
def popularposts():
    posts= Post.objects.filter(Status= True).order_by('Published_Date')[:4]
    Context= {'posts': posts}
    return Context

@register.simple_tag
def Past_Time(Published_Date):
    Current_Time= timezone.localtime(timezone.now())
    past_time=  Current_Time - Published_Date
    return past_time