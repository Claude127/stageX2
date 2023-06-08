from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.

# gestion de connexion et deconnexion de comptes
def login_user(request):
    # recupère l'email de l'utilisateur a partir du cookie , s'il est present
    email = request.COOKIES.get('email', '')

    # traitement du formulaires
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            response = redirect('file')

            if remember:
                response.set_cookie('email', email, max_age=14 * 24 * 60 * 60)  # cookie valable pendant 2 semaines
                return response
        else:
            messages.error(request, 'valeurs incorrectes, veuillez réessayer...')
            return redirect('login')
    else:
        # afficher la page de connexion avec l'email prerempli s'il existe
        return render(request, 'login.html',{'email': email})


def logout_user(request):
    logout(request)

    response = redirect('login')
    response.delete_cookie('email')
    messages.success(request, 'you were logged out :)')
    return response('login')


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


def add_user(request):
    return render(request, 'admin/add_user.html')


def profile_mod(request):
    return render(request, 'profile_mod.html')
