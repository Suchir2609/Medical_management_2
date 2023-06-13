from django.shortcuts import render,redirect
from .models import Room
from django.contrib.auth.decorators import login_required


def room_list(request):
    return render(request, 'users/room_list.html')


def room(request, room_name):
    return render(request, "users/room.html", {"room_name": room_name})


# def checkview(request):
#     room = request.POST('room_name')
#     username = Room.user.username
#
#     if Room.objects.filter(name=room).exists():
#         return redirect('/' + room+'/?username='+username)
#     else:
#         new_room = Room.objects.create(name=room)
#         new_room.save()
#         return redirect('/'+room+'/?username='+username)
