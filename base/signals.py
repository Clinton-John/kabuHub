from django.contrib.auth.models import User
from .models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from django.core.mail import send_mail
from django.conf import settings

def createProfile(sender, instance,  created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email
        )
        subject = 'Welcome to Kabu Hub'
        message = 'we are glad to have you join the community'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently= false,
        )
        
