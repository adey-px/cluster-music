from django.shortcuts import render, redirect, get_object_or_404
from music.models import Audio

# Create your views here.


# Pro subscription upgrade view
def upgrade(request):
    """ A view that renders upgrade template """

    return render(request, 'checkout/upgrade.html')


# Checkout page view
def checkout(request):
    """ A view that renders checkout template   """

    return render(request, 'checkout/checkout.html')


# Checkout success view
def checkout_success(request):
    """ A view that renders checkout success template """

    return render(request, 'checkout/checkout_success.html')


# Download access view
def download_access(request):
    """ A view that renders download access template """

    audios = Audio.objects.all()
    context = {}
    context['audios'] = audios

    return render(request, 'checkout/download.html', context)
