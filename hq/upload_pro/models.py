from django.db import models

# Create your models here.


class project(models.Model):
    projectowner = models.CharField(max_length = 30)
    project_name = models.CharField(max_length = 30)
    project_description = models.TextField(max_length = 30)
    file = models.FileField(max_length = 100)
    uploadtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "projects"
