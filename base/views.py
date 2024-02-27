from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm
from django.contrib.auth import login , authenticate , logout
from .models import User , Event , Sport_Event , Team
from .forms import EventForm , UserProfileForm , SportsForm , TeamForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import Group
from .decoraters import unauthenticated_user, allowed_users


#---------------------------Basic Website Functions ------------------------------

def home(request):
   events = Event.objects.all()[0:3]
   second_events = Event.objects.all()[4:8]
   # general_events = Event.objects.filter(topic=q)
   # law_events = Event.objects.filter(topic='LAW')
   # kubsa_events = Event.objects.filter(topic='KUBSA')
   # kuesa_events = Event.objects.filter(topic='KUESA')
   # sset_events = Event.objects.filter(topic='SSET')
   # smhs_events = Event.objects.filter(topic='SMHS')

   sports_events = Sport_Event.objects.all()

   group = Group.objects.get(name='super_admin')
   admin_group = Group.objects.get(name='Admins')
   sports_admins = Group.objects.get(name='sports_admins')
   
   sports_admins_users = sports_admins.user_set.all()
   admin_group_users = admin_group.user_set.all()
   group_super_admin = group.user_set.all()


   context = {'events':events,'second_events':second_events, 'group_super_admin':group_super_admin, 'admin_group_users':admin_group_users, 'sports_admins_users':sports_admins_users, 'sports_events':sports_events}
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

@unauthenticated_user
def loginPage(request):
   page = 'login'

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



#---------------------------User Profile functions ------------------------------
def userProfile(request, pk):
   user = User.objects.get(id=pk)
   events = user.event_set.all()


   context = {'user':user, 'events':events}
   return render(request, 'base/profile.html', context)

@login_required(login_url='login')
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
def deleteUser(request, pk):
   user = user.objects.get(id=pk)

   if request.method == 'POST':
      user.delete()
      return  redirect('home')

   return render(request, 'base/delete.html' , {'obj' :user})



#---------------------------Website Event functions ------------------------------

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def addEvent(request):
    event_form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event_instance = form.save(commit=False)
            event_instance.created_by = request.user
            event_instance.save()
            return redirect('home')

    context = {'event_form': event_form}
    return render(request, 'base/event_form.html', context)

def viewEvent(request, pk):
   page = 'EventUpdate'
   event = Event.objects.get(id=pk)
   group = Group.objects.get(name='super_admin')
   group_super_admin = group.user_set.all()


   context = {'event':event, 'group_super_admin':group_super_admin, 'page':page}
   return render(request, 'base/event.html', context)

@login_required(login_url="login")
def updateEvent(request, pk):
   page = 'EventUpdate'
   event = Event.objects.get(id=pk)
   update_form = EventForm(instance=event)
   if request.method == 'POST':
      form = EventForm(request.POST,request.FILES, instance=event)
      if form.is_valid():
         form.save()
         return redirect('view_event' , pk=event.id)
      
   context = {'update_form':update_form , 'page':page}
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

#---------------------------Sports Event Functions ------------------------------
@login_required(login_url="login")
@allowed_users(allowed_roles=['sports_admins','super_admin'])
def addSportsEvent(request):
   event_form = SportsForm()
   if request.method == 'POST':
      form = SportsForm(request.POST, request.FILES)
      if form.is_valid():
         event_instance = form.save(commit=False)
         event_instance.created_by = request.user
         event_instance.save()
         return redirect('home')

   context = {'event_form': event_form}
   return render(request, 'base/event_form.html', context)

def viewSportEvent(request, pk):
   event = Sport_Event.objects.get(id=pk)
   group = Group.objects.get(name='super_admin')
   group_super_admin = group.user_set.all()
   context = {'event':event, 'group_super_admin':group_super_admin}
   return render(request, 'base/event.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['sports_admins'])
def updateSportsEvent(request, pk):
   page = 'SportsUpdate'
   sports_event = Sport_Event.objects.get(id=pk)
   update_form = SportsForm(instance=sports_event)
   if request.method == 'POST':
      form = EventForm(request.POST,request.FILES, instance=user)
      if form.is_valid():
         form.save()
         return redirect('view_event' , pk=event.id)
      
   context = {'update_form':update_form, 'page':page}
   return render(request,'base/update_profile_new.html', context)

@login_required(login_url="login")
def deleteSportsEvent(request, pk):
   event = Sport_Event.objects.get(id=pk)

   if request.user != event.created_by:
      return HttpResponse("you cant update the room !!!") 

   if request.method == 'POST':
      event.delete()
      return  redirect('home')

   return render(request, 'base/delete.html' , {'obj' :event})



   return render(request, 'base/delete.html' , {'obj' :user})

#---------------------------Sports League Functions ------------------------------
@login_required(login_url="login")
@allowed_users(allowed_roles=['sports_admins'])
def addTeam(request):
   team_form = TeamForm()
   if request.method == 'POST':
      form = TeamForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('manage_league_table')

   context = {'team_form':team_form}
   return render(request, 'base/team_form.html', context)

def viewTable(request):
   teams = Team.objects.all()
   context = {'teams':teams}
   return render(request, 'base/league.html', context)
@login_required(login_url="login")
@allowed_users(allowed_roles=['sports_admins'])
def manageLeagueTable(request):
   teams = Team.objects.all().order_by('team_name')
   context = {'teams':teams}

   return render(request, 'base/league_administration.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['sports_admins'])
def updateTeam(request, pk):
   team = Team.objects.get(id=pk)
   update_form = TeamForm(instance=team)
   if request.method == 'POST':
      form = TeamForm(request.POST, instance=team)
      if form.is_valid():
         form.save()
         return redirect('manage_league_table')
   context = {'update_form':update_form}
   return render(request, 'base/update_profile.html', context)

#---------------------------Admin and Admins Page Functions ------------------------------
@login_required(login_url="login")
def adminsPage(request):
    group = Group.objects.get(name='super_admin')
    group_users = group.user_set.all()

    admin_group = Group.objects.get(name='Admins')
    admin_group_users = admin_group.user_set.all()

    sports_admins = Group.objects.get(name='sports_admins')
    sports_admins_users = sports_admins.user_set.all()

    context = {'group_users':group_users, 'sports_admins_users':sports_admins_users, 'admin_group_users':admin_group_users}
    return render(request , 'base/admins_page.html' , context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['super_admin'])
def changeRole(request):
   #  message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except:
            HttpResponse("User with the provided email doesnt exist")
            # message = "User with the provided email doesnt exist"
            # return redirect('change_role')
    
        users_group = Group.objects.get(name='Students')
        if users_group not in user.groups.all():
            return HttpResponse("The user isnt registered in the website")
            
        user.groups.remove(users_group)

        admin_group = Group.objects.get(name='Admins')
        user.groups.add(admin_group)

        return redirect('admins_page')

    context = {}
    return render(request , 'base/change_role.html' , context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['super_admin'])
def addSportsAdmin(request):
   # message = None
   if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except:
            
            return HttpResponse("The user isnt registered in the website")
            message = "The user with the registered email doesnt exist"
            return redirect('add_sports_admin')
    
        users_group = Group.objects.get(name='Students')
        if users_group not in user.groups.all():
            return HttpResponse("The user isnt registered in the website")
            
        user.groups.remove(users_group)

        sports_admin_group = Group.objects.get(name='sports_admins')
        user.groups.add(sports_admin_group)

        return redirect('admins_page')

   context = {}
   return render(request , 'base/change_role.html' , context)


