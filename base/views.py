from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm
from django.contrib.auth import login , authenticate , logout
from .models import User , Event
from .forms import EventForm , UserProfileForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import Group

# Create your views here.

def home(request):
   events = Event.objects.all()
   group = Group.objects.get(name='super_admin')
   group_users = group.user_set.all()
   context = {'events':events, 'group_users':group_users}
   return render(request , 'base/home.html', context)

def signup(request):
    page = 'signup'

    if request.user.is_authenticated:
      return redirect('home')

    form = MyUserCreationForm()
    
    if request.method == 'POST':
      form = MyUserCreationForm(request.POST)
      if form.is_valid():
         user = form.save(commit=False)
         user.username = user.username.lower()
         user.save()

         group = Group.objects.get(name='Students')
         user.groups.add(group)
         username = form.cleaned_data.get('username')
         messages.success(request, f'Account successfully created for {username}')

         login(request, user)
         return redirect('home')
      # else:
      #    messages.error(request , 'An error has occured during registration')


    context = {'page':page, 'form':form}
    return render(request , 'base/login_register_new.html', context)

def loginPage(request):
   page = 'login'

   if request.user.is_authenticated:
      return redirect('home')
   

   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      try:
         user = User.objects.get(username=username)
         user = authenticate(request, username=username , password=password)
         if user is not None:
            login(request, user)
            return redirect('home')
      except:
         messages.error(request, 'User does not exist')

    #   user = authenticate(request, username=username , password=password)

    #   if user is not None:
    #      login(request, user)
    #      return redirect('home')
         messages.error(request, 'Username or Password doesnt exist')


   context = {'page':page}
   return render(request, 'base/login_register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def addEvent(request):
   event_form = EventForm()
   if request.method == 'POST':

      Event.objects.create(
         created_by = request.user,
         title = request.POST.get('title'),
         date = request.POST.get('date'),
         description = request.POST.get('description')

      )
      return redirect('home')

   context = {'event_form':event_form}
   return render(request, 'base/event_form.html', context)

def userProfile(request, pk):
   user = User.objects.get(id=pk)
   events = user.event_set.all()
   context = {'user':user, 'events':events}
   return render(request, 'base/profile.html', context)


def updateProfile(request):
   user = request.user
   update_form = UserProfileForm(instance=user)
   if request.method == 'POST':
      form = UserProfileForm(request.POST,request.FILES, instance=user)
      if form.is_valid():
         form.save()
         return redirect('user-profile' , pk=user.id)
      

 
   context = {'update_form':update_form}
   return render(request,'base/update_profile_new.html', context)

@login_required(login_url='login')
def deleteEvent(request, pk):
   event = Event.objects.get(id=pk)

   if request.user != event.created_by:
      return HttpResponse("you cant update the room !!!") 

   if request.method == 'POST':
      event.delete()
      return  redirect('home')

   return render(request, 'base/delete.html' , {'obj' :event})

@login_required(login_url='login')
def deleteUser(request, pk):
   user = user.objects.get(id=pk)

   if request.method == 'POST':
      user.delete()
      return  redirect('home')

   return render(request, 'base/delete.html' , {'obj' :user})

def adminsPage(request):
    group = Group.objects.get(name='super_admin')
    group_users = group.user_set.all()
    
    context = {'group_users':group_users}
    return render(request , 'base/admins_page.html' , context)


def changeRole(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except:
            HttpResponse("User with the provided email doesnt exist")
    
        users_group = Group.objects.get(name='Students')
        if users_group not in user.groups.all():
            return HttpResponse("The user isnt registered in the website")
            
        user.groups.remove(users_group)

        admin_group = Group.objects.get(name='Admins')
        user.groups.add(admin_group)

        return redirect('admins_page')

    context = {}
    return render(request , 'base/change_role.html' , context)