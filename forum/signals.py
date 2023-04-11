from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.models import EmailAddress
from .models import FUser


@receiver(post_save, sender=EmailAddress)
def new_user(instance, **kwargs):
    try:
        fuser = FUser(email=instance.user, name='User', avatar='default_avatar.jpg')
        fuser.save()
    except:
        pass
