from django.shortcuts import render
from . models import Rooms
# from django.http import HttpResponse

# Create your views here.
def rooms(request):
    rooms = Rooms.objects.all()

    context = {
        'rooms' : rooms
    }

    return render(request, 'rooms/rooms.html', context)

