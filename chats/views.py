from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import Serializer
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *


@api_view(["GET"])
def chatRoom(request, current_id, receiver_id):
    try:
        chat_room = ChatRoom.objects.get(
            current_user=current_id, receiver_user=receiver_id)
    except ObjectDoesNotExist:
        chat_room = ChatRoom.objects.get(
            current_user=receiver_id, receiver_user=current_id)
    current_user = get_user_model().objects.get(id=current_id)
    receiver_user = get_user_model().objects.get(id=receiver_id)
    if (current_user and receiver_user) in chat_room.users.all():
        serializer = ChatRoomSerializer(chat_room, many=False)
        return Response(serializer.data)
    return Response({""})


@api_view(["GET", "POST"])
def createChatRoom(request, current_id, receiver_id):
    current_user = get_user_model().objects.get(id=current_id)
    receiver_user = get_user_model().objects.get(id=receiver_id)
    try:
        try:
            chat_room = ChatRoom.objects.get(
                current_user=current_user, receiver_user=receiver_user)
        except ObjectDoesNotExist:
            chat_room = ChatRoom.objects.get(
                current_user=receiver_user, receiver_user=current_user)

        serializer = ChatRoomSerializer(chat_room, many=False)

    except ObjectDoesNotExist:
        chat_room = ChatRoom.objects.create(current_user=current_user,
                                            receiver_user=receiver_user)
        chat_room.users.add(current_user)
        chat_room.users.add(receiver_user)
        chat_room.save()
        serializer = ChatRoomSerializer(chat_room, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def allChats(request):
    chats = ChatRoom.objects.all()
    serializer = ChatRoomSerializer(chats, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def messages(request, chat_room):
    messages = Message.objects.filter(chat_room=chat_room).all().order_by("id")
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def sendMessage(request, chat_room, user):
    text = request.data['text']
    user = get_user_model().objects.get(
        id=user)
    Message.objects.create(user=user, chat_room=ChatRoom.objects.get(
        id=chat_room), text=text)
    return Response({"message": "Message sent"})
