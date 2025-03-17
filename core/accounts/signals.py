from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs["created"]:
        user_instance = kwargs["instance"]
        Profile.objects.create(id=user_instance.id, user=user_instance)
