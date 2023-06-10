from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


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
            print(user)
        else:
            messages.error(request, 'valeurs incorrectes, veuillez réessayer...')
            return redirect('login')
            print(user)

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
    if user:
        nom = user.nom
        prenom = user.prenom
        img = user.image.name
        return render(request, 'file.html', {'nom': nom, 'prenom': prenom, 'img': img})
    else:
        return redirect('login')


@login_required(login_url='/login')
@permission_required('labfile.can_view_site')
def add_file(request):
    # recuperer les informations de l'utilisateur connecté
    user = request.user
    if user:
        nom = user.nom
        prenom = user.prenom,
        img = user.image.name
        return render(request, 'admin/add_file.html', {'nom': nom, 'prenom': prenom, 'img': img})
    else:
        return redirect('login')

@login_required(login_url='/login')
def view_file(request):
    # recuperer les informations de l'utilisateur connecté
    user = request.user
    if user:
        nom = user.nom
        prenom = user.prenom
        img = user.image.name
        return render(request, 'view_file.html', {'nom': nom, 'prenom': prenom, 'img': img})
    else:
        return redirect('login')


@login_required(login_url='/login')
@permission_required('labfile.can_view_site')
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
def add_user(request):
    return render(request, 'admin/add_user.html')
