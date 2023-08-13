from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Profile, Settings, User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_user_settings(sender, instance, created, **kwargs):
    if created:
        Settings.objects.create(user=instance)
