from django.shortcuts import render
from django.http import HttpResponse
from events.models import events_list
from signup.models import signup_user


def Feeds(request):
    updates =events_list.objects.all()
    online_users = []

    filler = signup_user.objects.filter(logstatus=True)
    for user in filler:
        print(user.First_Name)
        online_users.append(user.First_Name)

    return render(request , "./Feeds/feeds.html" , context = {"updates" : updates,"online_users":online_users})
