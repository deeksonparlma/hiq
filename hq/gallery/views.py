from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def photos(request):
    return HttpResponse("Hello world")


def uploadphotos(request):
    return HttpResponse("uploading")
