
from django.contrib import admin
from django.urls import path
from .views import welcome, length, weight, temperature

urlpatterns = [
    path('', welcome, name = 'welcome'),
    path('length/', length, name = 'length'),
    path('weight/', weight, name = 'weight'),
    path('temperature/', temperature, name = 'temperature'),
]
