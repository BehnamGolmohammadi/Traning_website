from django import template
register= template.Library()
from blog.models import Post


@register.simple_tag
def Latestpost():
    posts= Post.objects.filter(Status= True).order_by('Published_Date')[:6]
    Context= {'posts': posts}
    return Context


@register.filter
def Short_Content(Content,Len= 35):
    return ' '.join(Content.split()[:Len]) + ' ...'

@register.inclusion_tag('website/home-Recentblogposts.html')
def Latestposts():
    posts= Post.objects.filter(Status= True).order_by('-Published_Date')[:6]
    Context= {'posts': posts}
    return Context