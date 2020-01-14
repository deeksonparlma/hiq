from django.conf.urls import url
from . import views
app_name = "upload"

urlpatterns = [
    url("^$" , views.upload , name = "upload"),
    url("projects/" , views.projects , name = "projects")

]
