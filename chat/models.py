from django.conf import settings
from django.db import models
from user.models import CustomUser


class Message(models.Model):

    receivers = models.ManyToManyField(
        CustomUser,
        blank=True,
        help_text='Hold down “Shift”, to select all or more than one serial instances quickly.'
    )

    title = models.CharField(max_length=150)

    message = models.TextField()

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updatedMessages',
        related_query_name='updatedMessage',
        editable=False
    )

    updated_datetime = models.DateTimeField(
        null=True,
        blank=True,
        editable=False
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='createdMessages',
        related_query_name='createdMessage',
        editable=False
    )

    created_datetime = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return '%s' % self.title


# from django.db.models.signals import post_save
from django.dispatch import receiver
from notification.models import Notification
from apis.shortcuts import push_notification
from django.db.models.signals import m2m_changed


@receiver(m2m_changed, sender=Message.receivers.through)
def create_notification_when_receivers_set(sender, instance, action, **kwargs):
    if action == 'post_add':
        data = {
            'title': instance.title,
            'message': instance.message,
            'user': {
                'id': instance.created_by.id,
                'name': instance.created_by.email
            }
        }
        notification = Notification.objects.create(data=data, created_by=instance.created_by)
        receivers = instance.receivers.all()
        notification.receivers.set(receivers)
        push_notification(receivers)


# @receiver(post_save, sender=Message)
# def create_notification(sender, instance=None, created=False, **kwargs):
#     if created:
#         data = {
#             'title': instance.title,
#             'message': instance.message,
#             'user': {
#                 'id': instance.created_by.id,
#                 'name': instance.created_by.email
#             }
#         }
#         notification = Notification.objects.create(data=data, created_by=instance.created_by)
#         receivers = instance.receivers.all()
#         notification.receivers.set(receivers)
#         push_notification(receivers)



