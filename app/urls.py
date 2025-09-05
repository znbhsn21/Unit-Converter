
from django.contrib import admin
from django.urls import path
from .views import welcome, length

urlpatterns = [
    path('', welcome, name = 'welcome'),
    path('/length', length, name = 'length'),
]
