from django.shortcuts import render, redirect
from music.models import Audio

# Create your views here.


def index(request):
    """ A view that renders home page with all audio songs """
    songs = Audio.objects.all()

    context = {
        "songs": songs
    }

    return render(request, 'home/index.html', context)
