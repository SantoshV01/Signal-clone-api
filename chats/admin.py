from django.contrib import admin
from .models import Message, ChatRoom


class MessageAdmin(admin.ModelAdmin):
    list_display = ['user']


class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ['current_user', 'receiver_user']


admin.site.register(Message, MessageAdmin)
admin.site.register(ChatRoom, ChatRoomAdmin)
