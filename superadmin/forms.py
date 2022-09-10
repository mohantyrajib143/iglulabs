from superadmin.models import tbl_departments
from django import forms

class DepartmentsForm(forms.ModelForm):
    class Meta:
        model = tbl_departments
        fields = '__all__'