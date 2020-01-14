from django.shortcuts import render,redirect
from .models import signup_user
# Create your views here.

def signup(request):
    if request.method == "POST":

        signup_user.objects.create(First_Name = request.POST["fname"] , Second_name  = request.POST['sname'] ,
         Password = request.POST['password'] , profilepic = request.FILES['profile'], Email = request.POST['email'] , Phone_Number = request.POST['pnumber'])
        return render(request , "./login/login.html")

    else:
        return render(request , "./signup/signup.html")
