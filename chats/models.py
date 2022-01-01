from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


class ChatRoom(models.Model):
    current_user = models.ForeignKey(
        get_user_model(), models.CASCADE, related_name="current_user")
    receiver_user = models.ForeignKey(
        get_user_model(), models.CASCADE, related_name="receiver_user")
    users = models.ManyToManyField(get_user_model())


class Message(models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, models.CASCADE)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to=f'chat/{datetime.now}/', blank=True, null=True)
