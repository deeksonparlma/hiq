from django import forms
from .models import project


class uploadform(forms.ModelForm):
    class Meta:
        model = project
        fields = ["project_name" , "project_description" , "file"]
