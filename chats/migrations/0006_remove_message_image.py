# Generated by Django 4.0 on 2021-12-29 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0005_message_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='image',
        ),
    ]
