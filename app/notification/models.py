"""
Define all the models that app is needed.
"""
import pytz
from django.db import models


class Distribution(models.Model):
    mailing_launch = models.DateTimeField()
    description = models.TextField(unique=True)
    mobile_code = models.CharField(max_length=10)
    mailing_end = models.DateTimeField()

    def __str__(self):
        return str(self.description)

    class Meta:
        ordering = ['mailing_launch']


class Client(models.Model):

    TIMEZONES_CHOICES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    phone_number = models.CharField(max_length=255, unique=True)
    mobile_code = models.CharField(max_length=10)
    time_zone = models.CharField(
        max_length=255,
        choices=TIMEZONES_CHOICES,
        default='UTC'
    )

    def __str__(self):
        return self.phone_number

    class Meta:
        ordering = ['phone_number']


class Message(models.Model):
    SENT_STATUS_PENDING = 'P'
    SENT_STATUS_COMPLETE = 'C'
    SENT_STATUS_FAILED = 'F'

    SENT_STATUS_CHOICES = [
        (SENT_STATUS_PENDING, 'Pending'),
        (SENT_STATUS_COMPLETE, 'Complete'),
        (SENT_STATUS_FAILED, 'Failed'),
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    sent_status = models.CharField(
        max_length=1,
        choices=SENT_STATUS_CHOICES,
        default=SENT_STATUS_PENDING
    )
    distribution = models.ForeignKey(
        Distribution,
        on_delete=models.CASCADE,
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return str(self.created_at)

    class Meta:
        ordering = ['created_at']
