from superadmin.models import *
from django import forms

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('id', 'name', 'description', )