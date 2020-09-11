from django.db import models
from django.utils import timezone
# Create your models here.
class Users(models.Model):
    email = models.EmailField(max_length=100,null=True)
    name = models.CharField(max_length=100,null=True)
    username = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.name
    
class UserData(models.Model):
    userid= models.IntegerField()
    name = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')
    profile_pic=models.ImageField(null=True,blank=True)
    def __str__(self):
        return '{}{}'.format(self.userid,self.location)