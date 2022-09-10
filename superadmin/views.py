from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'superadmin/index.html')

def dashboard(request):
    return render(request,'superadmin/dashboard.html')

def employees_list(request):
    return render(request,'superadmin/employees_list.html')

def employees_grid(request):
    return render(request,'superadmin/employees_grid.html')
