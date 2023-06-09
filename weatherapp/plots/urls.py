from django.contrib import admin
from django.urls import path
from plots.views import weather_data_panel

urlpatterns = [
    path('', weather_data_panel),
    path('<str:location>', weather_data_panel),
]