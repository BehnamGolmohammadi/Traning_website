from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    x="""
<head>
<h1 style='color: #116c91'>
Main Page
<h1/>
<body>
<h2 style='color: #9820bd'>
Welcome to Main page
<h2/>
<body/>
<head/>
"""
    return HttpResponse(x)


def page1(request):
    x="""
<head>
<h1 style='color: #116c91'>
Page 1
<h1/>
<body>
<h2 style='color: #9820bd'>
Welcome to page 1
<h2/>
<body/>
<head/>
"""
    return HttpResponse(x)


def page2(request):
    x="""
<head>
<h1 style='color: #116c91'>
Page 2
<h1/>
<body>
<h2 style='color: #9820bd'>
Welcome to page 2
<h2/>
<body/>
<head/>
"""
    return HttpResponse(x)


def page3(request):
    x="""
<head>
<h1 style='color: #116c91'>
Page 3
<h1/>
<body>
<h2 style='color: #9820bd'>
Welcome to page 3
<h2/>
<body/>
<head/>
"""
    return HttpResponse(x)