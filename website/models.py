import django
from django.db import models
from django.forms import EmailField

# Create your models here.
class Contact(models.Model):
    Name= models.CharField(max_length= 50)
    Email= models.EmailField()
    Subject= models.CharField(max_length= 255)
    Message= models.TextField()
    Created_Date= models.DateTimeField(auto_now_add= True)
    Updated_Date= models.DateTimeField(auto_now= True)