from superadmin.models import tbl_departments, tbl_designations, tbl_holidays, tbl_assets
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

class AssetsForm(forms.ModelForm):
    class Meta:
        model = tbl_assets
        fields = ('emp_id', 'assets_name', 'assets_id', 'mouse_id', 'keyboard_id', 'assets_info', 'status')
    def __init__(self, *args, **kwargs):
        super(AssetsForm, self).__init__(*args, **kwargs)
        self.fields['mouse_id'].required = False
        self.fields['keyboard_id'].required = False