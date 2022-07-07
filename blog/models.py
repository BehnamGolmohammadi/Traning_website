from operator import mod
from django.db import models

# Create your models here.
class Post(models.Model):
    # Image
    # auther
    Title= models.CharField(max_length= 255)
    Content= models.TextField()
    # tag
    # category
    Counted_view= models.IntegerField(default= 0)
    Status= models.BooleanField(default= False)
    Published_Date= models.DateTimeField(null= True)
    Created_Date= models.DateTimeField(auto_now_add= True)
    Update_Date= models.DateTimeField(auto_now= True)