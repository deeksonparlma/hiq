from django.shortcuts import render,redirect

from signup.models import signup_user
from .forms import loginfrm
# Create your views here.
def login(request):
    form = loginfrm()
    error_var = ""
    sess = ""

    if request.method == 'POST':
        try:
            logstats = signup_user.objects.get(Email = request.POST['email'])

        except:

            error_var = "no user with name exists"

        else:
            if logstats.Password == request.POST["password"]:

                request.session["username"] = logstats.First_Name

                logstats.logstatus = True
                logstats.save()
                # print()

                # request.session["email"] = signup_user.objects.get(Email = request.POST['email'])


                # set the username of the currrent user
                sess = request.session["username"]
                # set the session variable email address
                request.session["email"] = request.POST['email']

                # Expires immediately th user exits the browser
                request.session.set_expiry(0)

                # redirect users to their profile page
                return redirect("profile/")
            else:
                error_var = "Wrong password"
    else:
        pass



    return render (request , "./login/login.html" , context = {"form": form , "error":error_var ,"sess":sess})
