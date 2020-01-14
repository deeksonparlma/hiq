from django.shortcuts import render
from upload_pro.models import project
# Create your views here.


def profile_viewer(request):
    # print(request.sesssion.has_key("username"))
    uname = ""
    try:
        uname = request.session["username"]

    except:
        uname = "You are not yet logged in."
    return render(request , "./uprofile/profile.html" , context = {"projects":project.objects.filter(projectowner = uname), "username":uname})



def update(request):
    return render(request , "./uprofile/update.html")


def project_viewer(request):
    pass
