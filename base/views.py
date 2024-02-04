from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm
# Create your views here.

def home(request):
    return render(request , 'base/home.html')

def signup(request):
    page = 'signup'
    form = MyUserCreationForm()
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')


    context = {'page':page, 'form':form}
    return render(request , 'base/login.html', context)

def login(request):
    page = 'login'

    context = {'page':page}
    return render(request , 'base/login.html' , context)

