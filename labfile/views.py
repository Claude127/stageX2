from pathlib import Path

import magic
import textract
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import path

from .models import Document, Categorie


# Create your views here.

# gestion de connexion et deconnexion de comptes

def login_user(request):
    # recuperer les informations du formulaire
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        # si la case remember est cochée, definir les cookies
        if remember:
            response = redirect('file')
            response.set_cookie('email', email, max_age=14 * 24 * 60 * 60)  # cookie valable pendant 2 semaines
            response.set_cookie('password', password, max_age=14 * 24 * 60 * 60)  # cookie valable pendant 2 semaines

        else:  # sinon la case est decochée, supprimer les cookies s'ils existent deja

            response = redirect('file')
            response.delete_cookie('email')

        user = authenticate(request, email=email, password=password)  # authentifier l'utilisateur
        if user is not None:

            login(request, user)
            return response  # rediriger l'utilisateur vers la page souhaitée

        else:
            messages.error(request, 'valeurs incorrectes, veuillez réessayer...')
            return redirect('login')


    else:
        # verifier si l'utilisateur est deja connecté
        if 'email' in request.COOKIES:
            return redirect('file')

        # verifier si des cookies sont presents pour l'email et le mot de passe

        email = request.COOKIES.get('email')
        password = request.COOKIES.get('password')

        # si des cookies sont presents se connecter automatiquement
        if email and password:

            user = authenticate(request, email=email, password=password)  # authentifier l'utilisateur
            if user is not None:
                login(request, user)
                return redirect('file')  # rediriger l'utilisateur vers la page souhaitée

        return render(request, 'login.html')


def logout_user(request):
    # supprimer la session de l'utilisateur
    logout(request)
    # supprimer les cookies pour l'email et le mot de passe
    response = redirect('login')
    response.delete_cookie('email')
    response.delete_cookie('password')
    # retourner un message de validation et la page de connexion
    messages.success(request, 'you were logged out :)')
    return response


# gestion des fichiers
@login_required(login_url='/login')
def file(request):
    user = request.user
    files = Document.objects.all()
    cat = Categorie.objects.all()
    if user:
        nom = user.nom
        prenom = user.prenom
        img = user.image.name
        return render(request, 'file.html', {'nom': nom, 'prenom': prenom, 'img': img, 'files': files, 'cats': cat})
    else:
        return redirect('login')


@login_required(login_url='/login')
@permission_required('labfile.can_view_site', raise_exception=True)
def add_file(request):
    if request.method == 'POST':


        #traiter les requetes
        name = request.POST.get('name')
        categorie = request.POST.get('categorie')
        cat_id = Categorie.objects.get(nom=categorie)
        emplac = request.FILES.get('emplac')
        user_id = request.user
        file = Document(nom=name, categorie=cat_id, emplacement=emplac, utilisateur=user_id)
        # sauvegarder les infos dans la bd
        file.save()
        return redirect('file')

    else:
        user = request.user
        # recuperer les informations de l'utilisateur connecté
        if user:
            nom = user.nom
            prenom = user.prenom
            img = user.image.name
            return render(request, 'admin/add_file.html', {'nom': nom, 'prenom': prenom, 'img': img})



@login_required(login_url='/login')
def view_file(request, file_id):
    # recuperer les informations de l'utilisateur connecté
    user = request.user
    file = Document.objects.get(pk=file_id)

    # definir le chemin d'acces au fichier
    file_path = Path(settings.MEDIA_ROOT, str(file.emplacement))

    # # detecter le jeu de caracteres du fichier
    # with open(file_path, 'rb') as f:
    #     file_type = magic.from_buffer(f.read(), mime=True)

    # extraire le texte du fichier
    file_contents = textract.process(str(file_path))

    if user:
        nom = user.nom
        prenom = user.prenom
        img = user.image.name
        return render(request, 'view_file.html', {'nom': nom, 'prenom': prenom, 'img': img, 'file': file,
                                                  'file_contents': file_contents})
    else:
        return redirect('login')


@login_required(login_url='/login')
@permission_required('labfile.can_view_site', raise_exception=True)
def file_mod(request):
    # recuperer les informations de l'utilisateur connecté
    user = request.user
    if user:
        nom = user.nom
        prenom = user.prenom
        img = user.image.name
        return render(request, 'admin/file_mod.html', {'nom': nom, 'prenom': prenom, 'img': img})
    else:
        return redirect('login')


# gestion des profils
@login_required(login_url='/login')
def profile(request):
    # recuperer les informations de l'utilisateur connecté
    user = request.user
    if user:
        nom = user.nom
        prenom = user.prenom
        img = user.image.name
        email = user.email
        return render(request, 'profile.html', {'nom': nom, 'prenom': prenom, 'img': img, 'email': email})
    else:
        return redirect('login')


@login_required(login_url='/login')
def profile_mod(request):
    # recuperer les informations de l'utilisateur connecté
    user = request.user
    if user:
        nom = user.nom
        prenom = user.prenom
        img = user.image.name
        email = user.email
        return render(request, 'profile_mod.html', {'nom': nom, 'prenom': prenom, 'img': img, 'email': email})
    else:
        return redirect('login')


@login_required(login_url='/login')
@permission_required('labfile.can_view_dashboard', raise_exception=True)
def dashboard(request):
    # recuperer les informations de l'utilisateur connecté
    user = request.user
    if user:
        nom = user.nom
        prenom = user.prenom
        img = user.image.name
        return render(request, 'admin/dashboard.html', {'nom': nom, 'prenom': prenom, 'img': img})
    else:
        return redirect('login')


@login_required(login_url='/login')
def user_admin(request):
    return render(request, 'admin/user_admin.html')


@login_required(login_url='/login')
def search(request):
    # fonction de recherche
    if request.method == 'POST':
        searched = request.POST.get('searched')
        files = Document.objects.filter(nom__contains=searched)
        user = request.user
        if user:
            nom = user.nom
            prenom = user.prenom
            img = user.image.name
            return render(request, 'search.html',
                          {'nom': nom, 'prenom': prenom, 'img': img, 'searched': searched, 'files': files})
    else:
        return redirect('login')
