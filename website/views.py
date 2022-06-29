from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'website/index.html')


def page1(request):
    return render(request, 'website/a.html')


def page2(request):
    return render(request, 'website/b.html')

def page3(request):
    return render(request, 'website/c.html')