# Generated by Django 3.2.15 on 2022-09-23 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['label']},
        ),
    ]
