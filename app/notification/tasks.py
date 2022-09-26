"""
Creating tasks for sending messages for clients.
"""
import os
import requests
from django.core.mail import BadHeaderError
from templated_mail.mail import BaseEmailMessage
from celery import shared_task
from .models import Message


BASE_URL = os.environ.get('BASE_URL')
TOKEN = os.environ.get('TOKEN')


@shared_task
def send_distribution(data, base_url=BASE_URL, token=TOKEN):
    message_id = data['id']
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    full_url = base_url + str(message_id)
    try:
        response = requests.post(url=full_url, headers=headers, json=data)
        print(response.content)
    except requests.exceptions.RequestException as exc:
        raise exc
    else:
        Message.objects.filter(pk=message_id).update(sent_status='C')


@shared_task
def send_report():
    queryset = Message.objects \
        .select_related('distribution') \
        .select_related('client') \
        .all()
    try:
        message = BaseEmailMessage(
            template_name='emails/report.html',
            context={
                'messages': list(queryset),
            },
        )
        message.send(['test2@example.com'])
    except BadHeaderError as error:
        raise error
