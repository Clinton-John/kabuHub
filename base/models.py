from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
# creating models section

# class User(AbstractUser):
#     name = models.CharField(max_length=200, null=True)
#     email = models.EmailField(unique=True, null=True)
#     bio = models.TextField(null=True)

#     # avatar = models.ImageField(null=True , default="avatar.svg")
#     # USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS = []

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # avatar = models.ImageField(null=True , default="avatar.svg")
    date = models.DateField()
    updated = models.DateTimeField(auto_now= True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name




