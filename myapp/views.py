from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"index.html")
def movie(request):
    return render(request,"moviesingle.html")