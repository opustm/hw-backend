from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class User(AbstractUser):
    picture=models.CharField(max_length=100, default='pic1')
    theme=models.CharField(max_length=100, default='theme1')
    phone=models.IntegerField(default=9119119111)


class MyGroup(Group):
    picture=models.CharField(max_length=100, default='pic1')
    announcement=models.CharField(max_length=100, default='This is a group')


    
# class User(models.Model):
#     firstName= models.CharField(max_length=100)
#     lastName= models.CharField(max_length=100)
#     picture=models.CharField(max_length=100)
#     theme=models.CharField(max_length=100)
#     phone=models.IntegerField()
#     email = models.EmailField(max_length=100, unique=True)
#     group = models.ManyToManyField(Group)

#     def __str__(self):
#         return self.name