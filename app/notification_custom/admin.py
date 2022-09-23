from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from tags.models import TagItem
from notification.admin import ClientAdmin
from notification.models import Client


class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TagItem
    extra = 0


class CustomClientAdmin(ClientAdmin):
    inlines = [TagInline]


admin.site.unregister(Client)
admin.site.register(Client, CustomClientAdmin)
