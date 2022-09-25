"""
Creating signals for Notification models.
"""
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Distribution, Client, Message
from .tasks import send_distribution


@receiver(post_save, sender=Distribution)
def distribution_post_save(sender, instance, created, **kwargs):
    if created:
        clients = Client.objects.filter(
            phone_number__istartswith=instance.mobile_code
        )
        current_datetime = timezone.now()

        for client in clients:
            new_message = Message.objects.create(
                distribution=instance,
                client=client,
            )

            payload = {
                'id': new_message.id,
                'phone': client.phone_number,
                'text': instance.description,
            }

            if instance.mailing_end >= current_datetime and \
                    instance.mailing_launch <= current_datetime:
                send_distribution.apply_async(
                    (payload,),
                    expires=instance.mailing_end
                )
            else:
                send_distribution.apply_async(
                    (payload,),
                    eta=instance.mailing_launch,
                    expires=instance.mailing_end
                )
