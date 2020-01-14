from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import eventfrm
from .models import events_list
# Create your views here.


def events(request):

    event_var = events_list.objects.all()

    try:
        sess = request.session["username"]

    except:

        sess = ""

    return render(request , "./events/events.html" , context = {"events":event_var, "username":sess})

def add_event(request):

    if request.method=='POST':
        try:
            uname = request.session["username"]

        except:

            uname = "Anornymous"

        events_list.objects.create(event_organizer = uname , event_description = request.POST["event_description"])
        return redirect("/events/")

    else:
        return render(request , "./events/addevents.html" , context = {"events":eventfrm})
        pass
