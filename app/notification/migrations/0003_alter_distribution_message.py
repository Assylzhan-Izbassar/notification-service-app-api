# Generated by Django 3.2.15 on 2022-09-24 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20220923_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='message',
            field=models.TextField(unique=True),
        ),
    ]
