from django.urls import path
from .views import *
app_name= 'website'

urlpatterns = [
    path('', index, name= 'index'),
    path('about', about, name= 'about'),
    path('contact', contact, name= 'contact'),
    path('newsletter', newsletter, name= 'newsletter')
    ]