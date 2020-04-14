from django.contrib import admin
from django.urls import path
import firstapp.views

urlpatterns = [
    path('', firstapp.views.home, name='home'),
    path('profile/', firstapp.views.profile, name='profile'),
    path('main/', firstapp.views.main, name='main'),
]
