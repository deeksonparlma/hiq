from django.shortcuts import render
from django.http import HttpResponse
from events.models import events_list
from signup.models import signup_user


def Feeds(request):
    updates = events_list.objects.order_by("-event_post_date")
    online_users = []

    filler = signup_user.objects.filter(logstatus=True)

    for user in filler:

        online_users.append(user.First_Name)
    # print(online_users)

    return render(request , "./Feeds/feeds.html" , context = {"updates" : updates,"online_users":online_users})
