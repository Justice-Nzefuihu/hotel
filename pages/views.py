from django.shortcuts import render
from rooms.models import Rooms
# from django.http import HttpResponse

# Create your views here.
def index(request):
    # rooms = Rooms.objects.order_by("-reg-date")
    rooms = Rooms.objects.all()[:3]

    context = {
        'rooms' : rooms
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
