from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from .models import Price


# Create your views here.


def upgrade(request):
    """ A view that renders home page with all audio songs """

    return render(request, 'checkout/upgrade.html')


def checkout(request):
    """ A view that renders home page with all audio songs """

    return render(request, 'checkout/checkout.html')
