from django.http import HttpResponse
from django.shortcuts import render, redirect
import pymysql
from django.contrib.auth import login
from django.contrib import messages

rm = ''
em = ''
pwd = ''

from .models import Utilisateur


# Create your views here.

# gestion de connexion et deconnexion de comptes
def login_user(request):
    # global em, pwd,rm
    # if request.method == 'POST':
    #
    #     # etablir la connexion a la base de donnees
    #     conn = pymysql.connect(
    #         host='localhost',
    #         user='root',
    #         password='',
    #         db='labfile',
    #         port=3306
    #     )
    #     # recupere les informations du formulaire
    #     d = request.POST
    #     for key, value in d.items():
    #         if key == "email":
    #             em = value
    #         if key == "password":
    #             pwd = value
    #         if key == "remember":
    #             rm =value
    #     # remember me
    #     if rm:
    #         # cas:case "se souvenir de moi" est cochee, definir un cookie
    #         max_age = 14*24*60*60 #la duree du cookie est de 14jours
    #         response = redirect('file')
    #         response.set_cookie('em', em, max_age=max_age)
    #         response.set_cookie('pwd', pwd, max_age=max_age)
    #     else:
    #         # cas: case "se souvenir de moi" est decochee ,supprimer les cookies
    #         response = redirect('file')
    #         response.delete_cookie('em')
    #         response.delete_cookie('pwd')
    #
    #     #executer la commande pour authentifier l'utilisateur
    #     c = "select * from labfile_utilisateur where email='{}' and password='{}' ".format(em, pwd)
    #     # curseur pour executer la commande
    #     cursor = conn.cursor()
    #     cursor.execute(c)
    #     t = tuple(cursor.fetchall())
    #     if t == ():
    #         messages.success(request, "une erreur est survenue , veuillez reesayer...")
    #         return redirect('login')
    #     else:
    #         request.session['email'] = em
    #         return response
    #         # verif session ouverte
    #         # message = f"Bienvenue,{em}!"
    #         # return HttpResponse(message)
    # else:
    #     #l'utilisateur est deja connecté
    #     if 'em' in request.session:
    #         return redirect('file')
    #     #verifier si les cookie sont presents
    #     em = request.COOKIES.get('em')
    #     pwd = request.COOKIES.get('pwd')
    #
    #     #si les cookies sont operationels ,se connecter automatiquement
    #
    #     if em and pwd:
    #         # etablir la connexion a la base de donnees
    #         conn = pymysql.connect(
    #             host='localhost',
    #             user='root',
    #             password='',
    #             db='labfile',
    #             port=3306
    #         )
    #         # executer la commande pour authentifier l'utilisateur
    #         c = "select * from labfile_utilisateur where email='{}' and password='{}' ".format(em, pwd)
    #         # curseur pour executer la commande
    #         cursor = conn.cursor()
    #         cursor.execute(c)
    #         t = tuple(cursor.fetchall())
    #         if t == ():
    #             messages.success(request, "une erreur est survenue , veuillez reesayer...")
    #             return redirect('login')
    #         else:
    #             request.session['email'] = em
    #             return redirect('file')
    #             # verif session ouverte
    #             # message = f"Bienvenue,{em}!"
    #             # return HttpResponse(message)
        #afficher la page de connexion
        return render(request, 'login.html')


def logout_user(request):
    #supprimer la session de l'utilisateur actuel
    request.session.flush()

    #supprimer les cookies pour l'email er le mot de passe
    response =redirect('login')
    response.delete_cookie('em')
    response.delete_cookie('pwd')

    return response


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
