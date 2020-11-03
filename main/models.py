from django.db import models

# class Group(models.Model):
#     name = models.CharField(max_length=100)
#     picture=models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

    
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