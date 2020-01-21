from django.shortcuts import render
from django.http import HttpResponse
from .forms import loginfrm

# Create your views here.
def home(request):
    form = loginfrm()
    if "username" in request.session:
        lcontrol = True
    else:
        lcontrol = False
    return render (request , "./home/index.html" , context = {"form": form , "loginshow":lcontrol})


def handle404(request ,exception):
    return HttpResponse("Hello world")
