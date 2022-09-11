from superadmin.models import tbl_departments, tbl_designations
from django import forms

class DepartmentsForm(forms.ModelForm):
    class Meta:
        model = tbl_departments
        fields = '__all__'

class DesignationsForm(forms.ModelForm):
    class Meta:
        model = tbl_designations
        fields = '__all__'