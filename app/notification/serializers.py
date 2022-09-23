"""
Creating serializers for proper models.
"""
from rest_framework import serializers
from .models import Distribution, Client, Message


class DistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribution
        fields = [
            'id',
            'mailing_launch',
            'message',
            'mobile_code',
            'mailing_end',
        ]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'phone_number',
            'mobile_code',
            'time_zone',
        ]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'sent_status',
            'created_at',
            'client',
            'distribution',
        ]
