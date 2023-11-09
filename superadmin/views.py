from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

def projects(request):
    return render(request, 'superadmin/projects.html')