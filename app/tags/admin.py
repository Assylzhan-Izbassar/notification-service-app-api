"""
Registering tag models to admin.
"""
from django.contrib import admin
from . import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['label']
    list_per_page = 10
    search_fields = ['label']
