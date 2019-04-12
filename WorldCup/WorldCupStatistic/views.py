from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Event, Venue, Country


def events(request):
    all_events = Event.objects.all().order_by('date')
    context = {'events': all_events,}
    return render(request, "events.html", context) 


def venues(request):
    all_venues = Venue.objects.all().order_by('event')
    print(all_venues)
    context = {'venues': all_venues}
    return render(request, "venues.html", context) 


def countries(request):
    all_countries = Country.objects.all()
    context = {'countries': all_countries}
    return render(request, "countries.html", context)


def help(request):
    context = {}
    return render(request, "help.html", context)


def eventshelp(request):
    context = {}
    return render(request, "helpevents.html", context)


def countrieshelp(request):
    context = {}
    return render(request, "helpcountries.html", context)


def venueshelp(request):
    context = {}
    return render(request, "helpvenues.html", context)
