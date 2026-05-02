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
        "news_main": News.objects.filter(section="main"),
        "news_left": News.objects.filter(section="left"),
        "news_right": News.objects.filter(section="right"),
        "tweets": Tweet.objects.all(),
        "movies_theater_popular": MovieTheater.objects.filter(type="popular"),
        "movies_theater_coming": MovieTheater.objects.filter(type="coming"),
        "movies_tv_popular": MovieTv.objects.filter(type="popular"),
        "movies_tv_coming": MovieTv.objects.filter(type="coming"),
    }
    return render(request, 'newIndex.html', context)



def moviesingle(request):
    return render(request,"moviesingle.html")