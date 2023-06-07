from django.http import HttpResponse
from django.shortcuts import render, redirect
import pymysql
from django.contrib.auth import login
from django.contrib import messages

em = ''
pwd = ''

from .models import Utilisateur


# Create your views here.

#gestion de connexion et deconnexion de comptes
def login_user(request):
    global em, pwd
    if request.method == 'POST':

        # etablir la connexion a la base de donnees
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='labfile',
            port=3306
        )
        # recupere les informations du formulaire
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value
        c = "select * from labfile_utilisateur where email='{}' and password='{}' ".format(em, pwd)
        # curseur pour executer la commande
        cursor = conn.cursor()
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            messages.success(request, "une erreur est survenue , veuillez reesayer...")
            return redirect('login')
        else:
            request.session['email'] = em
            return redirect('file')
            #verif session ouverte
            # message = f"Bienvenue,{em}!"
            # return HttpResponse(message)
    else:
        return render(request, 'login.html')

def logout_user(request):
    if 'em' in request.session:
        del request.session['em']

    return redirect('login')






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
