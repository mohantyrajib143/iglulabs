from django.contrib import admin
from superadmin.models import tbl_departments, tbl_designations, tbl_holidays

# Register your models here.
admin.site.register(tbl_departments)
admin.site.register(tbl_designations)
admin.site.register(tbl_holidays)