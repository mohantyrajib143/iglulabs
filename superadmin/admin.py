from django.contrib import admin
from superadmin.models import tbl_departments, tbl_designations, tbl_holidays, tbl_assets, tbl_emp_family

# Register your models here.
admin.site.register(tbl_departments)
admin.site.register(tbl_designations)
admin.site.register(tbl_holidays)
admin.site.register(tbl_assets)
admin.site.register(tbl_emp_family)