from django.shortcuts import render
from django.http import HttpResponse
from .models import (
    Slider, Advertisement, SocialLink, Celebrity, Trailer
)

def home(request):
    context = {
        'sliders': Slider.objects.all(),
        'ads': Advertisement.objects.all(),
        'social_links': SocialLink.objects.all(),
        'celebrities': Celebrity.objects.all(),
        'trailers': Trailer.objects.all(),
    }
    return render(request, 'newIndex.html', context)

# 5 more needed (edit the html however u want)



def movie(request):
    return render(request,"moviesingle.html")