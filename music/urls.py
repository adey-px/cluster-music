from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('playing/', views.now_playing, name='now_playing'),
    path('upload/', views.upload_audio, name='upload_audio'),
    path('user_audios/', views.my_music, name='my_music'),
]
