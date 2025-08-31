from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from notifications.models import Notification
from .models import CustomUser

@receiver(m2m_changed, sender=CustomUser.followers.through)
def create_follow_notification(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        # instance is the user being followed
        # pk_set contains the primary key of the new follower
        follower_id = list(pk_set)[0]
        follower = CustomUser.objects.get(pk=follower_id)
        Notification.objects.create(
            recipient=instance,
            actor=follower,
            verb='started following you',
            target=follower
        )
