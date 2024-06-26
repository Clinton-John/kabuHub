# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Event , Profile, User , Sport_Event , Team
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1', 'password2']

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields ='__all__'
        exclude = ['created_by']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
class SportsForm(ModelForm):
    class Meta:
        model = Sport_Event
        fields ='__all__'
        exclude = ['created_by']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user'] 

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        exclude = ['']