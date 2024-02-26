from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
# creating models section

# class User(AbstractUser):
#     name = models.CharField(max_length=200, null=True)
#     email = models.EmailField(unique=True, null=True)
#     bio = models.TextField(null=True)

#     profile_pic = models.ImageField(null=True , blank=True)
# #     # USERNAME_FIELD = 'email'
# #     # REQUIRED_FIELDS = []

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    profile_pic = models.ImageField(default="avatar.svg", null=True , blank=True)

    def  __str__(self):
        return self.username
    


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    event_pic = models.ImageField(null=True , blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    date = models.DateField()
    updated = models.DateTimeField(auto_now= True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.event_pic.url
        except:
            url = ''
        return url

class Team(models.Model):
    team_name = models.CharField(max_length=128, unique=True)
    points = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    goals_against = models.IntegerField(default=0)
    goal_difference = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name

class Sport_Event(models.Model):
    sports_title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    sports_pic = models.ImageField(null=True , blank=True)
    venue = models.CharField(max_length=150, blank=True, null=True)
    date = models.DateField()
    updated = models.DateTimeField(auto_now= True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sports_title

    @property
    def imageURL(self):
        try:
            url = self.sports_pic.url
        except:
            url = ''
        return url




