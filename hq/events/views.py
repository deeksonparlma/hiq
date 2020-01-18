from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import eventfrm
from .models import events_list
# Create your views here.
from signup.models import signup_user

def events(request):

    event_var = events_list.objects.order_by("-event_post_date")
    # signup_user.objects.get()

    try:
        sess = request.session["username"]

    except:

        sess = ""

    return render(request , "./events/events.html" , context = {"events":event_var, "username":sess})

def add_event(request):
    errorlog = ""
    if request.method=='POST':
        try:
            uname = request.session["email"]

        except:
            errorlog = "Please login to continue"
            uname = "Anornymous"
            return render(request , "./events/addevents.html" , context = {"events":eventfrm,"errorlog":errorlog})
        else:

            n = signup_user.objects.get(Email = request.session["email"]).uid

            events_list.objects.create(event_organizer = 1, event_description = request.POST["event_description"])

            return redirect("/events/")

    else:
        return render(request , "./events/addevents.html" , context = {"events":eventfrm})
