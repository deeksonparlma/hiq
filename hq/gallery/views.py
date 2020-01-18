from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .forms import galform

from .models import HiQGallery

def photos(request):
    hqgallery = HiQGallery.objects.order_by("id")
    # uploaduser
    return render(request , "./gallery/photos.html" , context = {"gallery":hqgallery})


def uploadphotos(request):
    if request.method == "POST":
        HiQGallery.objects.create(uid_id = 1 ,image = request.FILES["image"])
        return redirect("/gallery")
    else:
        pass

    frm = galform
    return render(request , "./gallery/uploadgal.html" ,  context = {"up":frm})
