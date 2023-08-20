from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from budgets.models import Budget


@receiver(post_save, sender=User)
def create_user_budget(sender, instance, created, **kwargs):
    if created:
        Budget.objects.create(user=instance)
