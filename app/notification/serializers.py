"""
Creating serializers for proper models.
"""
from rest_framework import serializers
from .models import Distribution, Client, Message


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


class DistributionSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(
        many=True,
        read_only=True,
        source='message_set'
    )
    sent_count = serializers \
        .SerializerMethodField('count_sent_messages')

    class Meta:
        model = Distribution
        fields = [
            'id',
            'mailing_launch',
            'description',
            'mobile_code',
            'mailing_end',
            'sent_count',
            'messages',
        ]

    def count_sent_messages(self, distribution):
        return distribution.message_set.count()


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'phone_number',
            'mobile_code',
            'time_zone',
        ]
