from django.shortcuts import render

def main(request):
    return render(request, 'main.html', {})

def room(request, room_name):
    return render(request, 'chatroom.html', {
        'room_name':room_name
    })
    