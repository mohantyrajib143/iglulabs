from django.db import models

# Create your models here.
class Employees(models.Model):
    emp_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    iglu_email = models.CharField(max_length=100)
    personal_email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    aadhaar_no = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    doj = models.DateField()
    current_address = models.CharField(max_length=200)
    permanent_address = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="employees")
    is_active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return self.emp_id
    
class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return self.name