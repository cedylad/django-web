from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing


def band(request):
    bands = Band.objects.all()
    return render(request, 'listings/bands.html',{'bands': bands})


def listing(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html',{'listings': listings})


def about(request):
    return render(request, 'listings/about.html')
