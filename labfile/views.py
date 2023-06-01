from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def file(request):
    return render(request, 'file.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def user_admin(request):
    return render(request, 'user_admin.html')


def profile(request):
    return render(request, 'profile.html')


def add_file(request):
    return render(request, 'add_file.html')


def view_file(request):
    return render(request, 'view_file.html')


def file_mod(request):
    return render(request, 'file_mod.html')


def login(request):
    return render(request, 'login.html')