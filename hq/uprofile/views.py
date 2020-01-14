from django.shortcuts import render,redirect
from upload_pro.models import project
from signup.models import signup_user
# Create your views here.


def profile_viewer(request):
    # print(request.sesssion.has_key("username"))
    uname = ""
    try:
        uname = request.session["email"]
        print(signup_user.objects.get(Email = request.session["email"]).profilepic)

    except:

        uname = "You are not yet logged in."
        return redirect("/login/")

    else:
        userinfo = signup_user.objects.get(Email = request.session["email"])
        return render(request , "./uprofile/profile.html" , context = {"projects":project.objects.filter(projectowner = uname) ,"userinfo":userinfo , "profile": signup_user.objects.get(Email = request.session["email"]).profilepic, "username":uname})



def update(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        mail = request.POST["email"]
        phone = request.POST["pnumber"]

        uobject = signup_user.objects.get(Email = request.POST["email"])
        uobject.First_Name = fname
        uobject.Second_Name = lname
        uobject.Email = mail
        uobject.Phone_Number = phone
        request.session["username"] = uobject.First_Name
        uobject.save()

    return redirect("/profile/")


def project_viewer(request):
    pass
