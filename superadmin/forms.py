from superadmin.models import tbl_departments, tbl_designations, tbl_holidays
from django import forms

class DepartmentsForm(forms.ModelForm):
    class Meta:
        model = tbl_departments
        fields = '__all__'

class DesignationsForm(forms.ModelForm):
    class Meta:
        model = tbl_designations
        fields = '__all__'

class HolidaysForm(forms.ModelForm):
    class Meta:
        model = tbl_holidays
        fields = '__all__'