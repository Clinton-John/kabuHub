from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from django.core.mail import send_mail
from django.conf import settings

# @receiver(post_save, sender=Profile)
def createProfile(sender, instance,  created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email
        )
        subject = 'Welcome to Kabu Hub'
        message = 'we are glad to have you join the Kabarak Community.'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently= False,
        )

# @receiver(post_save, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
#the next signal to be added is one that sends an email to a user once the user's role is changed
post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
        
