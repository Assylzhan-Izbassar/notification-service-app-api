"""
Registering models to admin site.
"""
from django.contrib import admin
from django.db.models.aggregates import Count
from . import models


@admin.register(models.Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ['mailing_launch', 'message', 'mobile_code', 'sent_count']
    list_editable = ['message']
    list_per_page = 10
    list_filter = ['mailing_launch', 'mobile_code']
    ordering = ['mailing_launch', 'mailing_end']
    search_fields = [
        'mobile_code',
        'mailing_launch__day',
        'mailing_launch__month',
        'mailing_launch__year'
    ]

    @admin.display(ordering='sent_count')
    def sent_count(self, distribution):
        return distribution.sent_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            sent_count=Count('distributions')
        )


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'time_zone']
    list_per_page = 10
    search_fields = ['phone_number']


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    autocomplete_fields = ['distribution', 'client']
    list_display = ['created_at', 'sent_status']
    list_editable = ['sent_status']
    list_per_page = 10
    list_select_related = ['client']

    def client_phone(self, message):
        return message.client.phone_number
