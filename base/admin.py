from django.contrib import admin
from .models import Event, Profile, Sport_Event , Team , Topic

# Register your models here.
admin.site.register(Event)
admin.site.register(Profile)
admin.site.register(Team)
admin.site.register(Topic)
admin.site.register(Sport_Event)