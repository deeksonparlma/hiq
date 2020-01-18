from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import uploadform
from .models import project
from signup.models import signup_user



def projects(request):
    pro = project.objects.filter(uid = signup_user.objects.get(Email = request.session["email"])).order_by("uploadtime")
    return render(request , "./upload_pro/projects.html" , context = {"yourprojects":pro})



def delete_project(request , deletedp = "Nothing altered .... "):

    try:
        project.objects.get(project_name=deletedp).delete()

    except:
        pass


    return render(request , "./upload_pro/deletep.html" , context = {"pro_del":deletedp})




def upload(request):
    if request.method=='POST':

        project.objects.create(project_name = request.POST['project_name'] ,
        project_description = request.POST["project_description"] , uid = signup_user.objects.get(Email = request.session["email"]), file = request.FILES["file"])
        print(request.session["username"])

    else:
        print("Null and void")

    return render(request , './upload_pro/upload.html' , context = {"form":uploadform})
