
import string
from django.shortcuts import render, HttpResponse
from .models import Message, Room
from django.db.models import Q
from . import Encryption


def home(request):
    return render(request, "home.html")


def user_check(request):

    # Method to render our message intake HTML page and listing all the previous chat.

    Sender = request.POST['Sender']
    Receiver = request.POST['Receiver']
    secret_key = request.POST['secret_key']
    R_message = []

    if Room.objects.filter(Q(sender=Sender) & Q(receiver=Receiver)).exists():

        room_id = Room.objects.filter(Q(sender=Sender)&Q(receiver=Receiver))[0].id
        group = Room.objects.get(id=room_id).group
        r_room = Room.objects.filter(group=group)

        if len(r_room) > 1:

            r_message = Message.objects.filter(Q(room=r_room[0])|Q(room=r_room[1]))

        else:

            r_message = Message.objects.filter(room=r_room[0])

    else:
        new_room = Room.objects.create(sender=Sender,receiver=Receiver)
        new_room.save()
        room_id = new_room.id
        group = new_room.group
        r_room = Room.objects.filter(group=group)

        if len(r_room) > 1:

            r_message = Message.objects.filter(Q(room=r_room[0]) | Q(room=r_room[1]))

        else:

            r_message = Message.objects.filter(room=r_room[0])

    for i in r_message:
        R_message.append(Encryption.decrypt(i.body, secret_key, string.printable))

    return render(request, "messages.html", {"Id": room_id, "Required_message": R_message})


def send(request):

    # Method to save entries in our database

    body = request.POST['body']
    encrypted_body = Encryption.encrypt(body, string.printable)
    room_id = request.POST['Id']

    new_message = Message.objects.create(room=Room.objects.get(id=room_id), body=encrypted_body)
    new_message.save()
    return HttpResponse("Message sent")

