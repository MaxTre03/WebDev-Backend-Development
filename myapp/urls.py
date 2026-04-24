from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("moviesingle.html",views.movie,name="movie")
]