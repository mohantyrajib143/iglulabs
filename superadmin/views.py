from django.shortcuts import render, redirect
from django.http import HttpResponse
from superadmin.models import tbl_departments, tbl_designations
from django.contrib import messages
from . forms import DepartmentsForm, DesignationsForm

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

# employees views starts here
def employees_list(request):
    return render(request,'superadmin/employees_list.html')

def employees_grid(request):
    return render(request,'superadmin/employees_grid.html')
