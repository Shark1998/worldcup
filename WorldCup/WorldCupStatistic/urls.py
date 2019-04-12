from django.urls import path
from . import views

urlpatterns = [
    path('', views.events),
    path('venues', views.venues),
    path('countries', views.countries),
    path('help', views.help),
    path('helpevents', views.eventshelp),
    path('helpcountries', views.countrieshelp),
    path('helpvenues', views.venueshelp),
]
