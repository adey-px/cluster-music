from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Audio

# Create your views here.


def now_playing(request):
    """ A view that plays/pauses audio songs from db """

    interface = Paginator(Audio.objects.all(), 1)
    paging = request.GET.get('page')
    pagination = interface.get_page(paging)

    context = {
        "pagination": pagination
        }

    return render(request, 'music/now_playing.html', context)
