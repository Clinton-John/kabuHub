from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Event

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1', 'password2']

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields ='__all__'