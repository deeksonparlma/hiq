from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import uploadform
from .models import project

def upload(request):
    if request.method=='POST':
        project.objects.create(project_name = request.POST['project_name'] ,
        project_description = request.POST["project_description"] , projectowner = request.session["username"], file = request.FILES["file"])
        print(request.session["username"])
    else:
        print("Null and void")

    return render(request , "./upload_pro/upload.html" , context = {"form":uploadform})



def projects(request):
    return render(request , "./upload_pro/upload.html")
