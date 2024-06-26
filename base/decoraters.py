from django.shortcuts import redirect
from django.http import HttpResponse


def unauthenticated_user(view_func):
    def wrapper_func(request , *args , **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request , *args ,*kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decoraters(view_func):
        def wrapper_func(request , *args , **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request , *args , **kwargs)
            else:
                return HttpResponse("oops ^ 00~00 ^ !! You arent allowed to access this page..")

        return wrapper_func
    return decoraters
