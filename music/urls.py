from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('now_playing/', views.now_playing, name='now_playing'),
]
