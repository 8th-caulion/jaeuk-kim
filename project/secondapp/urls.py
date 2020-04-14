from django.contrib import admin
from django.urls import path
import secondapp.views



urlpatterns = [
    path('contact/', secondapp.views.contact, name='contact'),
    path('main/write/', secondapp.views.write, name='write'),
    
]



