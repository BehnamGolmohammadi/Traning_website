from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def page1(request):
    return render(request, 'a.html')


def page2(request):
    return render(request, 'b.html')

def page3(request):
    return render(request, 'c.html')