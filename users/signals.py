from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# The post-save signal will be called whenever the object is saved, either after creation or updating
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # The code in the if block needs to be run only if the user was created and not if the user was just updated.
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
