from django.shortcuts import render, redirect, get_object_or_404
from music.models import Audio
from django.http import HttpResponse


# Create your views here.


def upgrade(request):
    """ A view that renders home page with all audio songs """

    return render(request, 'checkout/upgrade.html')


def checkout(request):
    """ A view that  """

    return render(request, 'checkout/checkout.html')


def checkout_success(request):
    """ A view that  """

    return render(request, 'checkout/checkout_success.html')


# View that outputs all audios from db for download
def download_access(request):
    """ A view that """

    audios = Audio.objects.all()
    context = {}
    context['audios'] = audios

    return render(request, 'checkout/download.html', context)
