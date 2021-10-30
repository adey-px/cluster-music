from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Audio

from .forms import AudioForm

# Create your views here.


# View for uploading for playing audio songs
def now_playing(request):
    """ A view that plays/pauses audio songs from db """

    interface = Paginator(Audio.objects.all(), 1)
    paging = request.GET.get('page')
    pagination = interface.get_page(paging)

    songs = Audio.objects.all()

    context = {
        "pagination": pagination,
        "songs": songs
    }

    return render(request, 'music/now_playing.html', context)


# View for uploading or adding audio songs
def upload_audio(request):
    """ A view that uploads audio songs into db """

    # Note capture of .files to get in the images of the audio uploaded.
    # Based on django message levels in base.html, message.success, .error etc
    # .....will select template to use from includes/toasts directory
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New audio added successfully')
            return redirect('upload_audio')
        else:
            messages.error(request, 'Failed to add audio. Please try again.')
            return redirect('upload_audio')
    else:
        form = AudioForm()

    template = 'music/upload_audio.html'
    context = {
        'form': form
    }

    return render(request, template, context)


# View for storing user audios to individual user account
def my_music(request):
    """ A view that stores audio uploaded in user account """

    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)

        if form.is_valid():
            request.session['form'] = 'user_audio'
    else:
        form = AudioForm()

    user_audio = request.session.get('form')
    context = {
        'user_audio': user_audio
    }

    return render(request, 'music/my_music.html', context)
