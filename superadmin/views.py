from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from superadmin.models import *
from superadmin.forms import *
from django.shortcuts import get_object_or_404

# Create your views here.
def mylogin(request):
    if request.user.is_authenticated:
        return redirect('dashboard/')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        domain = email.split('@')[1]
        domain_list = ["iglulabs.com"]

        if domain not in domain_list:
            messages.error(request, 'Please, enter iglulabs email id..')
        else:
            if User.objects.filter(email=email).exists():
                username = User.objects.get(email=email.lower()).username
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Successfully Login!, redirecting...')
                else:
                    messages.error(request, 'password is not correct!')
            else:
                messages.error(request, 'Email or password is not correct!')
    return render(request, 'superadmin/login.html')

@login_required(login_url='mylogin')
def mylogout(request):
    logout(request)
    return redirect('mylogin')

def dashboard(request):
    return render(request, 'superadmin/dashboard.html')

@login_required(login_url='mylogin')
def projects(request):
    if request.method=='POST':
        name = request.POST['name']
        description = request.POST['description']

        if Projects.objects.filter(name=name).exists():
            messages.error(request, 'project name already exist!!')
        else:
            data = Projects(name=name, description=description)
            data.save()
            messages.success(request, 'Project saved successfully!')
        return redirect('projects')
    else:
        allData = Projects.objects.all().order_by('-id')
        data = {'allData':allData}
        return render(request, 'superadmin/projects.html', data)
    
@login_required(login_url='mylogin')
def editProjects(request, id):
    update = Projects.objects.get(id=id)
    query = ProjectsForm(request.POST, instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Projects updated successfully!')
    return redirect('projects')

@login_required(login_url='mylogin')
def updateProjectStatus(request, id):
    # Get the project instance
    project = get_object_or_404(Projects, id=id)

    # Toggle the value of is_active
    project.is_active = not project.is_active
    project.save()
    messages.success(request, 'Status updated successfully!')
    return redirect('projects')

@login_required(login_url='mylogin')
def deleteProjects(request, id):
    # Get the project instance or raise a 404 error if not found
    project = get_object_or_404(Projects, id=id)

    # Delete the project
    project.delete()
    messages.success(request, 'Projects deleted successfully!')
    return redirect('projects')