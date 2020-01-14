from django.conf.urls import url
from . import views

app_name = "upload"

urlpatterns = [
    url("delete_project/" , views.delete_project , name = "deleteP"),
    url("^$" , views.upload , name = "upload"),
    url("projects/" , views.projects , name = "projects"),

]
