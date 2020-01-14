from django.shortcuts import render
from django.http import HttpResponse
from signup.models import signup_user
# Create your views here.


def logout(request):
    try:
        try:
            print(request.session['email'])
            loguser = signup_user.objects.get(Email = request.session['email'])
            loguser.logstatus = 0
            loguser.save()

        except Exception as e:
            print("->>>> {}\n\n".format(e))
            # pass

        del request.session

    except:
        return HttpResponse("You are not logged in")
    else:
        return render(request , "./logout/logout.html")
