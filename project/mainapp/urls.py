from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('main/',views.main, name='main'),
   path('main/<int:blog_id>',views.detail, name='detail'),
   path('write/',views.write, name='write'),
   path('main/create/',views.create, name='create'),
   path('main/edit/<int:blog_id>',views.edit, name='edit'),
   path('main/update/<int:blog_id>',views.update, name='update'),
   path('main/delete/<int:blog_id>',views.delete, name='delete'),
]