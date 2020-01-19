from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .forms import galform

from .models import HiQGallery
from signup.models import signup_user

def photos(request):
    hqgallery = HiQGallery.objects.order_by("id")
    # uploaduser
    return render(request , "./gallery/photos.html" , context = {"gallery":hqgallery})




def uploadphotos(request):
    if request.method == "POST":
        try:
            HiQGallery.objects.create(uid_id = signup_user.objects.get(Email = request.session["email"]).uid ,
            image = request.FILES["image"])

            return redirect("/gallery")

        except KeyError as e:
            return redirect("/login/")

        else:
            pass

    else:
        pass

    frm = galform
    return render(request , "./gallery/uploadgal.html" ,  context = {"up":frm})
