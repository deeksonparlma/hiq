from django.db import models
# Create your models here.
from signup.models import signup_user

class project(models.Model):
    uid = models.ForeignKey(signup_user , on_delete = models.CASCADE)
    # projectowner = models.EmailField(max_length = 50)
    project_name = models.CharField(max_length = 30)
    project_description = models.TextField(max_length = 255)
    file = models.FileField(max_length = 100)
    uploadtime = models.DateTimeField(auto_now_add=True , null = True)

    class Meta:
        db_table = "projects"

    def __str__(self):
        return self.projectowner
