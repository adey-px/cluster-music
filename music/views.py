from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Case, When
from django.core.paginator import Paginator

from profiles.models import UserProfile
from .models import Audio

from .forms import AudioForm

# Create your views here.


# View for uploading or adding audio into db. Note attached user profile
def add_audio(request):
    """ A view that uploads audio songs into db """

    # Note capture of .files to get in the images of the audio uploaded.
    # Based on django message levels in base.html, message.success, .error etc
    # .....will select template to use from includes/toasts directory
    if request.method == 'POST':

        # First get UserProfile model, imported above, from profiles app
        user_profile = UserProfile.objects.get(user=request.user)

        # Check if form is submitted, then attach its data to current user
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(user_profile)
            messages.success(request, 'New audio added successfully')
            return redirect('add_audio')
        else:
            messages.error(request, 'Failed to add audio. Please try again.')
            return redirect('add_audio')
    else:
        form = AudioForm()

    template = 'music/add_audio.html'
    context = {
        'form': form
    }

    return render(request, template, context)


# View for playing audio songs existing in db
def now_playing(request, audio_id):
    """ A view that plays/pauses audio songs from db """

    # Get each audio to play by id from the db
    audio_playing = get_object_or_404(Audio, pk=audio_id)

    # Get all audios from db, making audio_playing always show 1st
    # using Conditional expressions - Case & When
    audios = Audio.objects.all().order_by(
        Case(When(pk=audio_playing.pk, then=0), default=1)
    )

    # Pass audios variable above into paginator - one audio per page
    interface = Paginator(audios, 1)
    paging = request.GET.get('page')
    pagination = interface.get_page(paging)

    # For right sidebar, get all audios from db to display them
    songs = Audio.objects.all()

    context = {
        "pagination": pagination,
        "active_audio": audio_playing,
        "songs": songs
    }

    return render(request, 'music/now_playing.html', context)


# View for displaying audio added by user in their own account
def my_audio(request):
    """ A view that displays audio. Get user profile and use it
    to filter all audio objects in the Audio model """

    # Get audios from db and filter them by current user profile
    user_profile = UserProfile.objects.get(user=request.user)
    audio = Audio.objects.filter(published_by=user_profile)

    context = {
        'user_audio': audio
    }

    return render(request, 'music/my_audio.html', context)


# View for editing uploaded audio by inidividual user
def edit_audio(request, audio_id):
    """ A view that edits audio """

    # Select audio by id from db to be edited
    audio = get_object_or_404(Audio, pk=audio_id)

    # Get form data with instance of the audio selected by its id
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES, instance=audio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your audio was edited successfully')
            return redirect('my_audio')
        else:
            messages.error(request, 'Failed to edit audio. Please try again.')
            return redirect('edit_audio')
    else:
        form = AudioForm(instance=audio)

    template = 'music/edit_audio.html'
    context = {
        'form': form,
        'audio': audio,
    }

    return render(request, template, context)


# View for deleting uploaded audio in individual user account
def delete_audio(request, audio_id):
    """ A view that edits audio uploaded in user account """

    # Select audio by id from db to be deleted
    audio = get_object_or_404(Audio, pk=audio_id)
    audio.delete()
    messages.success(request, 'Your audio has been deleted')

    return render(request, 'music/my_audio.html')


# View for saving favourite audio from db to user account
def saved_audio(request):
    """ A view that saves audio """

    return render(request, 'music/saved_audio.html')


# View for displaying play history to user account
def history(request):
    """ A view that gets play history """

    return render(request, 'music/history.html')
