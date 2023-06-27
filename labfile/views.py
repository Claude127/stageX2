
from django.contrib.auth.decorators import login_required, permission_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
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
        # si des cookies sont presents se connecter automatiquement
        if 'email' and 'password' in request.COOKIES:
            email = request.COOKIES.get('email')
            password = request.COOKIES.get('password')
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
    messages.success(request, 'vous etes déconnectés :)')
    return response


# gestion des fichiers
@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
@permission_required('labfile.can_view_site', raise_exception=True)
def add_file(request):
    if request.method == 'POST':

        # traiter les requetes
        name = request.POST.get('name')
        categorie = request.POST.get('categorie')
        cat_id = Categorie.objects.get(nom=categorie)
        emplac = request.FILES.get('emplac')
        lock = request.POST.get('lock', False) == 'on'
        user_id = request.user
        file = Document(nom=name, categorie=cat_id, is_lock=lock, emplacement=emplac, utilisateur=user_id)
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


@login_required(login_url='/login/')
def delete_file(request, file_id):
    user = request.user
    nom = user.nom
    prenom = user.prenom
    img = user.image.name
    file = Document.objects.get(pk=file_id)
    # traitement du fichier de suppression
    if request.method == 'POST':
        fs = FileSystemStorage()
        fs.delete(file.emplacement.name)
        file.delete()
        return redirect('file')
    else:
        return render(request, 'file.html', {'nom': nom, 'prenom': prenom, 'img': img})


@login_required(login_url='/login/')
@permission_required('labfile.can_view_site', raise_exception=True)
def file_mod(request, file_id):
    file = Document.objects.get(pk=file_id)
    if request.method == 'POST':
        nom = request.POST['name']
        categorie = request.POST['categorie']  # faire correspondre la categorie a son id
        cat_id = Categorie.objects.get(nom=categorie)

        # attribuons de nouvelles valeurs a l'element

        file.nom = nom
        file.categorie = cat_id

        file.save()
        return redirect('file')
    else:
        user = request.user
        if user:
            nom = user.nom
            prenom = user.prenom
            img = user.image.name
            return render(request, 'admin/file_mod.html', {'nom': nom, 'prenom': prenom, 'img': img, 'file': file})


# gestion des profils
@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def profile_mod(request):
    if request.method == 'POST':
        nom = request.POST['name']
        prenom = request.POST['surname']
        email = request.POST['email']
        image = request.FILES.get('image')
        old_password = request.POST['old-password']
        new_password1 = request.POST['new-password1']
        new_password2 = request.POST['new-password2']

        user = request.user

        if new_password1:

            if not user.check_password(old_password):
                messages.error(request, 'Ancien mot de passe invalide .')
                return redirect('profile_mod')
            elif new_password1 != new_password2:
                messages.error(request, 'les mots de passes ne correspondent pas')
                return redirect('profile_mod')
            else:
                user.nom = nom
                user.prenom = prenom
                user.email = email
                if image:
                    user.image = image
                user.set_password(new_password1)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
        else:
            if not user.check_password(old_password):
                messages.error(request, 'Ancien mot de passe invalide .')
            else:
                user.nom = nom
                user.prenom = prenom
                user.email = email
                if image:
                    user.image = image
            user.save()
            update_session_auth_hash(request, user)
            return redirect('profile')

    else:
        user = request.user
        if user:
            nom = user.nom
            prenom = user.prenom
            img = user.image.name
            email = user.email
            password = user.password
            return render(request, 'profile_mod.html',
                          {'nom': nom, 'prenom': prenom, 'img': img, 'email': email, 'password': password})


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def user_admin(request):
    return render(request, 'admin/user_admin.html')


@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def sort_files(request, category_id):
    category = Categorie.objects.get(pk=category_id)
    files = Document.objects.filter(categorie=category)
    cat = Categorie.objects.all()
    user = request.user
    if user:
        nom = user.nom
        prenom = user.prenom
        img = user.image.name

        return render(request, 'sort_files.html',
                      {'categorie': category, 'files': files, 'nom': nom, 'prenom': prenom, 'img': img, 'cats': cat})


def error404(request, exception):
    user = request.user
    if user:
        nom = user.nom
        prenom = user.prenom
        img = user.image.name

    return render(request, '404.html', {'prenom': prenom, 'nom': nom, 'img': img})
