from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .forms import uploadform
from .models import project
from signup.models import signup_user



def projects(request):
    pro = project.objects.filter(uid = signup_user.objects.get(Email = request.session["email"])).order_by("uploadtime")
    return render(request , "./upload_pro/projects.html" , context = {"yourprojects":pro})



def delete_project(request , deletedp = "Nothing altered .... "):
    otherprojects = ""

    try:
        # print(deletedp)
        project.objects.filter(project_name=deletedp).delete()

    except:
        pass

    else:
        # print(signup_user.objects.get(Email = request.session["email"]).Email)
        # print("Got the value ->> {}".format(signup_user.objects.get(Email = request.session["email"]).uid))
        otherprojects = project.objects.filter(uid = signup_user.objects.get(Email = request.session["email"])).order_by("uploadtime")
        # otherprojects = project.objects.filter(uid_id.uid = 5)
        # print(otherprojects)
        pass

    return render(request , "./upload_pro/deletep.html" , context = {"pro_del":deletedp,"otherpros":otherprojects})




def upload(request):
    if request.method=='POST':

        uname = ""
        try:
            uname = request.session["email"].split("@")[0]
            usern = request.session["username"]

        except:

            uname = "You are not yet logged in."
            return redirect("/login/")

        else:
            project.objects.create(project_name = request.POST['project_name'] ,
            project_description = request.POST["project_description"] , uid = signup_user.objects.get(Email = request.session["email"]), file = request.FILES["file"])
            print(request.session["username"])
            return redirect("profile/")

    else:
        print("Null and void")

        return render(request , './upload_pro/upload.html' , context = {"form":uploadform})
