from django.shortcuts import render

from .forms import loginfrm

# Create your views here.
def home(request):
    form = loginfrm()
    return render (request , "./home/index.html" , context = {"form": form})
