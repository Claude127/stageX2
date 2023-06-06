from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def file(request):
    return render(request, 'file.html')


def dashboard(request):
    return render(request, 'admin/dashboard.html')


def user_admin(request):
    return render(request, 'admin/user_admin.html')


def profile(request):
    return render(request, 'profile.html')


def add_file(request):
    return render(request, 'admin/add_file.html')


def view_file(request):
    return render(request, 'view_file.html')


def file_mod(request):
    return render(request, 'admin/file_mod.html')


def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('file')
        else:
            messages.success(request, "une erreur est survenue , veuilez reesayer...")
            return redirect('login')
    else:
        return render(request, 'login.html')


def add_user(request):
    return render(request, 'admin/add_user.html')


def profile_mod(request):
    return render(request, 'profile_mod.html')
