from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('playing/<audio_id>', views.now_playing, name='now_playing'),
    path('add_audio/', views.add_audio, name='add_audio'),
    path('user_audio/', views.my_audio, name='my_audio'),
    path('saved_audio/', views.saved_audio, name='saved_audio'),
    path('history/', views.history, name='history'),
]
