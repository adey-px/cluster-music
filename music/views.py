from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from profiles.models import UserProfile
from .models import Audio

from .forms import AudioForm

# Create your views here.


# View for playing audio songs existing in db
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


# View for uploading or adding audio into db. Note attached user profile
def add_audio(request):
    """ A view that uploads audio songs into db """

    # Note capture of .files to get in the images of the audio uploaded.
    # Based on django message levels in base.html, message.success, .error etc
    # .....will select template to use from includes/toasts directory
    if request.method == 'POST':

        # First get UserProfile model, imported above, from profiles app
        user_profile = UserProfile.objects.get(user=request.user)

        # Check if form is submitted, then capture its data into user profile
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


# View for displaying audio added by user in their own account
def my_audio(request):
    """ A view that displays audio uploaded in user account """

    profile = get_object_or_404(UserProfile, user=request.user)

    user_audio = request.session.get('audios')

    context = {
        'user_audio': user_audio,
        'profile': profile
    }

    return render(request, 'music/my_audio.html', context)


# View for editing uploaded audio in individual user account
def adit_audio(request):
    """ A view that deletes audio uploaded in user account """

    return render(request, 'music/edit_audio.html')


# View for deleting uploaded audio in individual user account
def delete_audio(request):
    """ A view that edits audio uploaded in user account """

    return render(request, 'music/my_audio.html')


# View for getting saved audio to individual user account
def saved_audio(request):
    """ A view that saves favourite audio into user account """

    return render(request, 'music/saved_audio.html')


# View for getting play history to individual user account
def history(request):
    """ A view that gets play history into user account """

    return render(request, 'music/history.html')
