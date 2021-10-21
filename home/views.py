from django.shortcuts import render, redirect
from . models import Audio

# Create your views here.


def index(request):
    """ A view that renders home page """
    songs = Audio.objects.all()

    context = {
        "songs": songs
    }

    return render(request, 'home/index.html', context)
