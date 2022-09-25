"""
Create celery config.
"""
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

celery = Celery('app')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()
