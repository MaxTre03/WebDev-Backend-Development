from django.shortcuts import render
from django.http import HttpResponse
from .models import (
    Slider, Advertisement, SocialLink, Celebrity, Trailer,TrailerItem,News,Tweet,MovieTheater,MovieTv
)

def home(request):
    context = {
        'sliders': Slider.objects.all(),
        'ads': Advertisement.objects.all(),
        'social_links': SocialLink.objects.all(),
        'celebrities': Celebrity.objects.all(),
        'trailers': Trailer.objects.all(),
        "trailer_items": TrailerItem.objects.all(),
        "news": News.objects.all(),
        "tweets": Tweet.objects.all(),
        "movies_theater": MovieTheater.objects.all(),
        "movies_tv": MovieTv.objects.all(),
    }
    return render(request, 'newIndex.html', context)





def movie(request):
    return render(request,"moviesingle.html")