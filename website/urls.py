from django.urls import path
from .views import index, page1, page2, page3

urlpatterns = [
    path('home', index),
    path('page1', page1),
    path('page2', page2),
    path('page3', page3)
]
