from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponse
from superadmin.models import tbl_departments, tbl_designations, tbl_holidays, tbl_assets, tbl_employee, tbl_emp_family
from django.contrib import messages
from . forms import DepartmentsForm, DesignationsForm, HolidaysForm, AssetsForm

# Create your views here.
def index(request):
    return render(request,'superadmin/index.html')

def dashboard(request):
    return render(request,'superadmin/dashboard.html')

# departments views starts here
def departments(request):
    if request.method=='POST':
        name = request.POST['name']
        status = request.POST['status']

        if tbl_departments.objects.filter(name=name).exists():
            messages.error(request, 'Department already exist!!')
        else:
            data = tbl_departments(name=name, status=status)
            data.save()
            messages.success(request, 'Department saved successfully!')
        return redirect('departments')
    else:
        allData = tbl_departments.objects.all().order_by('-id')
        data = {'allData':allData}
        return render(request, 'superadmin/departments.html', data)

def update_departments_status(request, id):
    query = tbl_departments.objects.get(id=id)
    if(query.status == 'active'):
        query.status = 'inactive'
    else:
        query.status = 'active'
    query.save()
    messages.success(request, 'Status updated successfully!')
    return redirect('departments')

def update_departments(request, id):
    update = tbl_departments.objects.get(id=id)
    name = request.POST['name']
    if tbl_departments.objects.filter(name=name).exists():
        messages.error(request, 'Department already exist!!')
    else:
        query = DepartmentsForm(request.POST, instance=update)
        query.save()
        if query.is_valid():
            query.save(commit=True)
            messages.success(request, 'Department updated successfully!')
    return redirect('departments')

def delete_departments(request, id):
    data = tbl_departments.objects.get(id=id)
    data.delete()
    messages.success(request, 'Department deleted successfully!')
    return redirect('departments')

# designations views starts here
def designations(request):
    if request.method=='POST':
        designation = request.POST['designation']
        departments = request.POST['departments']
        status = request.POST['status']

        if tbl_designations.objects.filter(name=designation, departments=departments).exists():
            messages.error(request, 'Designation already exist!!')
        else:
            data = tbl_designations(name=designation, departments=departments, status=status)
            data.save()
            messages.success(request, 'Designation saved successfully!')
        return redirect('designations')
    else:
        allDepartments = tbl_departments.objects.all().order_by('-id')
        allData = tbl_designations.objects.all().order_by('-id')
        data = {'allDepartments':allDepartments, 'allData':allData}
        return render(request, 'superadmin/designations.html', data)

def update_designation_status(request, id):
    query = tbl_designations.objects.get(id=id)
    if(query.status == 'active'):
        query.status = 'inactive'
    else:
        query.status = 'active'
    query.save()
    messages.success(request, 'Status updated successfully!')
    return redirect('designations')

def update_designation(request, id):
    update = tbl_designations.objects.get(id=id)
    name = request.POST['name']
    departments = request.POST['departments']
    if tbl_designations.objects.filter(name=name, departments=departments).exists():
        messages.error(request, 'Designation already exist!!')
    else:
        query = DesignationsForm(request.POST, instance=update)
        query.save()
        if query.is_valid():
            query.save(commit=True)
            messages.success(request, 'Designation updated successfully!')
    return redirect('designations')

def delete_designation(request, id):
    data = tbl_designations.objects.get(id=id)
    data.delete()
    messages.success(request, 'Designation deleted successfully!')
    return redirect('designations')

# holidays views starts here
def holidays(request):
    if request.method=='POST':
        title = request.POST['title']
        date = request.POST['date']
        status = request.POST['status']

        if tbl_holidays.objects.filter(date=date).exists():
            messages.error(request, 'Designation already exist!!')
        else:
            data = tbl_holidays(title=title, date=date, status=status)
            data.save()
            messages.success(request, 'Holiday saved successfully!')
        return redirect('holidays')
    else:
        allData = tbl_holidays.objects.all().order_by('-id')
        data = {'allData':allData}
        return render(request, 'superadmin/holidays.html', data)

def update_holidays_status(request, id):
    query = tbl_holidays.objects.get(id=id)
    if(query.status == 'active'):
        query.status = 'inactive'
    else:
        query.status = 'active'
    query.save()
    messages.success(request, 'Status updated successfully!')
    return redirect('holidays')

def update_holidays(request, id):
    update = tbl_holidays.objects.get(id=id)
    title = request.POST['title']
    date = request.POST['date']
    if tbl_holidays.objects.filter(title=title, date=date).exists():
        messages.error(request, 'Holiday already exist!!')
    else:
        query = HolidaysForm(request.POST, instance=update)
        query.save()
        if query.is_valid():
            query.save(commit=True)
            messages.success(request, 'Holidays updated successfully!')
    return redirect('holidays')

def delete_holidays(request, id):
    data = tbl_holidays.objects.get(id=id)
    data.delete()
    messages.success(request, 'Holiday deleted successfully!')
    return redirect('holidays')

# holidays views starts here
def assets(request):
    if request.method=='POST':
        emp_id = request.POST['emp_id']
        assets_name = request.POST['assets_name']
        assets_id = request.POST['assets_id']
        mouse_id = request.POST['mouse_id']
        keyboard_id = request.POST['keyboard_id']
        assets_info = request.POST['assets_info']
        status = request.POST['status']

        if tbl_assets.objects.filter(emp_id=emp_id).exists():
            messages.error(request, 'Employee ID already exist!!')
        else:
            data = tbl_assets(emp_id=emp_id, assets_name=assets_name, assets_id=assets_id, mouse_id=mouse_id, keyboard_id=keyboard_id, assets_info=assets_info, status=status)
            data.save()
            messages.success(request, 'Assets saved successfully!')
        return redirect('assets')
    else:
        allData = tbl_assets.objects.all().order_by('-id')
        data = {'allData':allData}
        return render(request, 'superadmin/assets.html', data)

def update_assets_status(request, id):
    query = tbl_assets.objects.get(id=id)
    if(query.status == 'active'):
        query.status = 'inactive'
    else:
        query.status = 'active'
    query.save()
    messages.success(request, 'Status updated successfully!')
    return redirect('assets')

def update_assets(request, id):
    update = tbl_assets.objects.get(id=id)
    query = AssetsForm(request.POST, instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Assets updated successfully!')
    return redirect('assets')

def delete_assets(request, id):
    data = tbl_assets.objects.get(id=id)
    data.delete()
    messages.success(request, 'Assets deleted successfully!')
    return redirect('assets')

# employees views starts here
def employees_list(request):
    if request.method=='POST':
        emp_id = request.POST['emp_id']
        team = request.POST['team']
        designation = request.POST['designation']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        aadhaar_no = request.POST['aadhaar_no']
        gender = request.POST['gender']
        dob = request.POST['dob']
        doj = request.POST['doj']
        current_address = request.POST['current_address']
        permanent_address = request.POST['permanent_address']
        nationality = request.POST['nationality']
        religion = request.POST['religion']
        marital_status = request.POST['marital_status']
        image = request.FILES['image']
        status = request.POST['status']

        data = tbl_employee(emp_id=emp_id, team=team, designation=designation, name=name, email=email, mobile=mobile, aadhaar_no=aadhaar_no, gender=gender, dob=dob, doj=doj, current_address=current_address, permanent_address=permanent_address, nationality=nationality, religion=religion, marital_status=marital_status, image=image, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('employees_list')
    else:
        empData = tbl_employee.objects.all().order_by('-id')
        data = {'empData':empData}
        return render(request, 'superadmin/employees_list.html', data)

def employees_grid(request):
    return render(request,'superadmin/employees_grid.html')

def employees_profile(request):
    EmpFamilyData = tbl_emp_family.objects.all().order_by('-id')
    data = {'EmpFamilyData':EmpFamilyData}
    return render(request,'superadmin/employees_profile.html', data)

def add_family_info(request):
    if request.method=='POST':
        emp_id = request.POST['emp_id']
        name = request.POST['name']
        relationship = request.POST['relationship']
        email = request.POST['email']
        mobile = request.POST['mobile']
        status = request.POST['status']

        data = tbl_emp_family(emp_id=emp_id, name=name, relationship=relationship, email=email, mobile=mobile, status=status)
        data.save()
        messages.success(request, 'Family member saved successfully!')
        return redirect('employees_profile')

def delete_emp_family_data(request, id):
    data = tbl_emp_family.objects.get(id=id)
    data.delete()
    messages.success(request, 'Family member deleted successfully!')
    return redirect('employees_profile')