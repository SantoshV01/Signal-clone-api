from django.urls import path
from .views import chatRoom, messages, sendMessage, allChats, createChatRoom

urlpatterns = [
    path("chatRoom/<str:current_id>/<str:receiver_id>/", chatRoom),
    path("createChatRoom/<str:current_id>/<str:receiver_id>/", createChatRoom),
    path("messages/<str:chat_room>/", messages),
    path("allChats/", allChats),
    path("sendMessage/<str:chat_room>/<str:user>/", sendMessage)
]
