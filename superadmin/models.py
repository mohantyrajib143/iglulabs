from django.db import models

# from superadmin.views import designations

# Create your models here.
class tbl_departments(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class tbl_designations(models.Model):
    name = models.CharField(max_length=100)
    departments = models.CharField(max_length=100)
    status = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class tbl_holidays(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class tbl_assets(models.Model):
    emp_id = models.CharField(max_length=100)
    assets_name = models.CharField(max_length=100)
    assets_id = models.CharField(max_length=100)
    mouse_id = models.CharField(max_length=100)
    keyboard_id = models.CharField(max_length=100)
    assets_info = models.CharField(max_length=500)
    status = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class tbl_employee(models.Model):
    emp_id = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.IntegerField()
    aadhaar_no = models.IntegerField()
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    doj = models.DateField()
    current_address = models.CharField(max_length=200)
    permanent_address = models.CharField(max_length=200)
    nationality = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100)
    image = models.ImageField(upload_to="employee")
    status = models.CharField(max_length=100, default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class tbl_emp_family(models.Model):
    emp_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    status = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)













    