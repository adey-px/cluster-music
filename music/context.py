from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import Audio


# Create bag_contents inside this context.py to get audio saved by user
# Add bag_contents name to settings.py to allow user save from any page
def bag_contents(request):

    bag_items = []

    context = {
        'bag_items': bag_items,
    }

    return context
